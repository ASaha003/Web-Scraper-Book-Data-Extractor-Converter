import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import random

# Define a static exchange rate (1 GBP to INR)
GBP_TO_INR_RATE = 105.50 

def scrape_books(url):
    # --- NEW: The Human Disguise ---
    # This header tells the website we are a normal Chrome browser, not a bot.
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    # Send a request to the website using our disguise
    response = requests.get(url, headers=headers)
    
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    books_data = []
    
    # Find all book containers on the page
    books = soup.find_all('article', class_='product_pod')
    
    # Loop through the containers to extract specific data
    for book in books:
        title = book.h3.a['title']
        price_raw = book.find('p', class_='price_color').text
        stock = book.find('p', class_='instock availability').text.strip()
        
        # Clean the price string and convert to INR
        price_clean = price_raw.replace('£', '').replace('Â', '').strip()
        price_numeric = float(price_clean)
        price_inr = price_numeric * GBP_TO_INR_RATE
        
        books_data.append({
            'Title': title,
            'Price (GBP)': price_raw,
            'Price (INR)': f"₹{price_inr:.2f}",
            'Availability': stock
        })
        
    return books_data

if __name__ == "__main__":
    URL = "http://books.toscrape.com/"
    
    print("Putting on our browser disguise...")
    
    # --- NEW: The Human Delay ---
    # Pause for a random amount of time (between 1 and 3 seconds) 
    # to mimic a human opening the browser and typing the URL.
    sleep_time = random.uniform(1.0, 3.0)
    print(f"Waiting for {sleep_time:.2f} seconds so we don't look suspicious...")
    time.sleep(sleep_time)
    
    print(f"Scraping data from {URL}...")
    
    # Run the scraper
    data = scrape_books(URL)
    
    # Convert the data to a Pandas DataFrame and save as CSV
    df = pd.DataFrame(data)
    df.to_csv('scraped_books.csv', index=False, encoding='utf-8')
    
    print(f"Success! {len(data)} books have been saved to 'scraped_books.csv'.")
    
    