from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator
import requests
import os
import time
import string
from collections import Counter


def scrape_elpais(driver):

    wait = WebDriverWait(driver, 20)
    driver.get("https://elpais.com/opinion/")

    # accept cookies
    try:
        cookie = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Aceptar') or contains(.,'Accept')]"))
        )
        cookie.click()
    except:
        pass

    os.makedirs("images", exist_ok=True)

    titles = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "h2 a"))
    )

    article_links = [t.get_attribute("href") for t in titles[:5] if t.get_attribute("href")]

    translated_titles = []

    for i, link in enumerate(article_links):
        try:
            print(f"\nProcessing article {i+1}")

            driver.get(link)

            # ⭐ wait for article load
            wait.until(
                EC.presence_of_element_located((By.TAG_NAME, "article"))
            )

            # cookie retry
            try:
                cookie = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Aceptar') or contains(.,'Accept')]"))
                )
                cookie.click()
            except:
                pass

            soup = BeautifulSoup(driver.page_source, "html.parser")

            # title
            title_tag = soup.find("h1")
            title = title_tag.get_text(strip=True) if title_tag else ""

            # translation retry
            translated_title = title
            for _ in range(2):
                try:
                    translated_title = GoogleTranslator(source='es', target='en').translate(title)
                    break
                except:
                    time.sleep(1)

            translated_titles.append(translated_title)

            # content
            paragraphs = soup.select("article p, div[data-dtm-region='articulo_cuerpo'] p")
            content = "\n".join([p.get_text(strip=True) for p in paragraphs if p.get_text(strip=True)])

            print("SPANISH TITLE:", title)
            print("ENGLISH TITLE:", translated_title)
            print("CONTENT PREVIEW:", content[:400])

            # ⭐ improved image extraction
            image_tag = soup.select_one("figure img, picture img, article img")

            if image_tag:
                img_url = (
                    image_tag.get("src")
                    or image_tag.get("data-src")
                    or image_tag.get("data-lazy-src")
                    or image_tag.get("srcset")
                )

                if img_url and "srcset" in image_tag.attrs:
                    img_url = image_tag["srcset"].split(",")[-1].split(" ")[0]

                if img_url and img_url.startswith("//"):
                    img_url = "https:" + img_url

                if img_url:
                    headers = {"User-Agent": "Mozilla/5.0"}
                    response = requests.get(img_url, headers=headers, timeout=10)

                    if response.status_code == 200:
                        session = driver.session_id or "local"
                        filename = f"images/article_{i}.jpg"
                        with open(filename, "wb") as f:
                            f.write(response.content)
                        print("Image downloaded")

            print("-----")

        except Exception as e:
            print("Error scraping:", link, e)

    # word frequency analysis
    cleaned = " ".join(translated_titles).lower().translate(
        str.maketrans('', '', string.punctuation)
    )
    word_counts = Counter(cleaned.split())

    print("\nRepeated words (>2 times):")
    for word, count in word_counts.items():
        if count > 2:
            print(word, ":", count)