# 📚 Web Scraper: Book Data Extractor & Converter

An automated Python web scraper that extracts product data from e-commerce websites. This project demonstrates foundational **Data Engineering** and **ETL (Extract, Transform, Load)** skills by gathering unstructured web data, applying transformations (like currency conversion), and exporting it into a clean, analytical format.

## ✨ Key Features
* **Humanized Scraping:** Uses custom `User-Agent` headers and randomized time delays (`time.sleep`) to mimic real human browsing behavior and avoid getting blocked by servers.
* **Live Data Extraction:** Parses HTML structures to target and extract specific elements (Titles, Prices, Stock Status).
* **Automated Currency Conversion:** Cleans raw string data (e.g., extracting numbers from "£51.77") and automatically converts British Pounds (GBP) to Indian Rupees (INR) using a defined exchange rate.
* **Structured Export:** Formats and exports the extracted data into a clean `.csv` file using Pandas, ready for data analysis or dashboarding.

## 🛠️ Tech Stack
* **Python 3**
* **BeautifulSoup4 (`bs4`)**: For HTML parsing and DOM navigation.
* **Requests**: For handling HTTP networking.
* **Pandas**: For data manipulation and CSV generation.
* **Time & Random**: For implementing human-like browsing delays.

## 🚀 How to Run Locally

### 1. Clone the repository
```bash
git clone [https://github.com/ASaha003/book-data-scraper.git](https://github.com/ASaha003/book-data-scraper.git)
cd book-data-scraper
