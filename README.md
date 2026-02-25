# 📰 El País BrowserStack Assignment

## 📌 Overview

This project demonstrates web scraping, translation, text analysis, and cross-browser automation using Selenium and BrowserStack.

The script visits the El País Opinion section, extracts article information, translates headers, downloads images, and performs repeated word analysis while executing tests across multiple browsers and devices.

---

## 🚀 Features Implemented

✅ Navigate to El País Opinion section (Spanish)
✅ Extract first 5 opinion articles
✅ Print Spanish title and article content
✅ Translate article titles to English
✅ Download cover images (if available)
✅ Perform repeated word frequency analysis on translated titles
✅ Execute cross-browser testing using BrowserStack
✅ Run parallel sessions across desktop and mobile environments

---

## 🛠️ Tech Stack

* Python
* Selenium WebDriver
* BeautifulSoup
* Requests
* Deep Translator
* BrowserStack Automate

---

## 📂 Project Structure

```
el-pais-task/
 ├── main.py
 ├── browserstack_test.py
 ├── images/
 ├── requirements.txt
 └── README.md
```

---

## ⚙️ Setup Instructions

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

## 🌐 Cross-Browser Coverage

The script runs on:

* Chrome (Windows)
* Firefox (Windows)
* Safari (macOS)
* Samsung Galaxy S22 (Android)
* iPhone 14 (iOS)

---

## 📝 Notes

* Images are downloaded only if available.
* Parallel execution depends on BrowserStack account concurrency limits.
* Translation is performed using GoogleTranslator API.
* Some image CDN failures may occur due to network restrictions and are handled gracefully.

---

## ✅ Assignment Requirements Coverage

✔ Spanish scraping
✔ Opinion article extraction
✔ Translation of headers
✔ Image download
✔ Word frequency analysis
✔ Cross-browser testing
✔ Parallel execution
✔ GitHub submission

---

## 👩‍💻 Author

**Kiran Dhuri**
