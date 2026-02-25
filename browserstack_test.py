from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from concurrent.futures import ThreadPoolExecutor
from main import scrape_elpais

USERNAME = "BROWSERSTACK_USERNAME"
ACCESS_KEY = "BROWSERSTACK_USERNAME"

BROWSERSTACK_URL = f"https://{USERNAME}:{ACCESS_KEY}@hub-cloud.browserstack.com/wd/hub"

caps_list = [
    {
        "browserName": "Chrome",
        "browserVersion": "latest",
        "bstack:options": {
            "os": "Windows",
            "osVersion": "11",
            "sessionName": "Chrome Test",
            "buildName": "ElPais Assignment",
            "projectName": "BrowserStack Hiring Task"
        }
    },
    {
        "browserName": "Firefox",
        "browserVersion": "latest",
        "bstack:options": {
            "os": "Windows",
            "osVersion": "10",
            "sessionName": "Firefox Test",
            "buildName": "ElPais Assignment",
            "projectName": "BrowserStack Hiring Task"
        }
    },
    {
        "browserName": "Safari",
        "browserVersion": "latest",
        "bstack:options": {
            "os": "OS X",
            "osVersion": "Ventura",
            "sessionName": "Safari Mac",
            "buildName": "ElPais Assignment",
            "projectName": "BrowserStack Hiring Task"
        }
    },
    {
        "browserName": "Chrome",
        "browserVersion": "latest",
        "bstack:options": {
            "deviceName": "Samsung Galaxy S22",
            "realMobile": True,
            "sessionName": "Android Chrome",
            "buildName": "ElPais Assignment",
            "projectName": "BrowserStack Hiring Task"
        }
    },
    {
        "browserName": "Safari",
        "browserVersion": "latest",
        "bstack:options": {
            "deviceName": "iPhone 14",
            "realMobile": True,
            "sessionName": "iPhone Safari",
            "buildName": "ElPais Assignment",
            "projectName": "BrowserStack Hiring Task"
        }
    }
]


def run_browserstack(cap):
    driver = None
    name = cap["bstack:options"]["sessionName"]

    try:
        print(f"🚀 Starting {name}")

        # ⭐ Selenium 4 correct capability handling
        options = Options()
        for key, value in cap.items():
            options.set_capability(key, value)

        driver = webdriver.Remote(
            command_executor=BROWSERSTACK_URL,
            options=options
        )

        scrape_elpais(driver)

        driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus",'
            '"arguments": {"status":"passed","reason": "Assignment completed"}}'
        )

    except Exception as e:
        print(f"❌ Error in {name}:", e)

        if driver:
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus",'
                '"arguments": {"status":"failed","reason": "Error occurred"}}'
            )

    finally:
        if driver:
            driver.quit()
            print(f"🛑 Closed {name}")


if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(run_browserstack, caps_list)