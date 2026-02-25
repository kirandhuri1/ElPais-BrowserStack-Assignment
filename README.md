# ⭐ El País BrowserStack Assignment

## 1.Overview

This project demonstrates web scraping, translation, text analysis, and cross-browser automation using Selenium and BrowserStack.

The script visits the El País Opinion section, extracts article information, translates headers, downloads images, and performs repeated word analysis while executing tests across multiple browsers and devices.

---

## 2. Features Implemented

1) Navigate to El País Opinion section (Spanish)
2) Extract first 5 opinion articles
3) Print Spanish title and article content
4) Translate article titles to English
5) Download cover images (if available)
6) Perform repeated word frequency analysis on translated titles
7) Execute cross-browser testing using BrowserStack
8) Run parallel sessions across desktop and mobile environments

---

## 3. Tech Stack

* Python
* Selenium WebDriver
* BeautifulSoup
* Requests
* Deep Translator
* BrowserStack Automate

---

## 4. Project Structure

```
el-pais-task/
 ├── main.py
 ├── browserstack_test.py
 ├── images/
 ├── requirements.txt
 └── README.md
```

---

## 5. Setup Instructions

### 1️⃣ Install dependencies

```
pip install selenium beautifulsoup4 requests deep-translator
```

---

### 2️⃣ Add BrowserStack credentials

Update inside `browserstack_test.py`:

```
USERNAME = "YOUR_BROWSERSTACK_USERNAME"
ACCESS_KEY = "YOUR_BROWSERSTACK_ACCESS_KEY"
```

---

### 3️⃣ Run BrowserStack tests

```
python browserstack_test.py
```

---

## 6.Cross-Browser Coverage

The script runs on:

* Chrome (Windows)
* Firefox (Windows)
* Safari (macOS)
* Samsung Galaxy S22 (Android)
* iPhone 14 (iOS)

---

## 7. Notes

* Images are downloaded only if available.
* Parallel execution depends on BrowserStack account concurrency limits.
* Translation is performed using GoogleTranslator API.
* Some image CDN failures may occur due to network restrictions and are handled gracefully.

---

## 8. Assignment Requirements Coverage

1) Spanish scraping
2) Opinion article extraction
3) Translation of headers
4) Image download
5) Word frequency analysis
6) Cross-browser testing
7) Parallel execution
8) GitHub submission

---

## Author

**Kiran Dhuri**
