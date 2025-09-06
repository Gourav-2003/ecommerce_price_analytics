from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import pandas as pd

# ChromeDriver path (update path as per your system)
CHROMEDRIVER_PATH = r"C:\Users\HP\Documents\tools\chromedriver-win64\chromedriver.exe"  # Replace with your chromedriver path

# Initialize Chrome driver
service = Service(CHROMEDRIVER_PATH)
driver = webdriver.Chrome(service=service)

# Product URLs (example URLs from your list)
urls = [
    'https://www.amazon.in/Samsung-Galaxy-Silver-128GB-Storage/dp/B0BZCR6TNK?th=1',
    'https://www.amazon.in/Mi-Vacuum-Mop-Powerful-Large-Capacity-Electronically-Controlled/dp/B0C1NYBYNQ',
    'https://www.amazon.in/PHILIPS-Fryer-NA120-00/dp/B08XYZ'  # Update with actual Philips Air Fryer URL
]

# Lists to hold scraped data
product_titles = []
product_prices = []
product_urls = []

for url in urls:
    driver.get(url)
    time.sleep(3)  # Wait for page to load
    
    try:
        # Extract product title
        title_element = driver.find_element(By.ID, 'productTitle')
        title = title_element.text.strip()
    except:
        title = "Title Not Found"
    
    try:
        # Extract price - Amazon uses different IDs, try common ones
        price_element = driver.find_element(By.ID, 'priceblock_ourprice')
    except:
        try:
            price_element = driver.find_element(By.ID, 'priceblock_dealprice')
        except:
            price_element = None

    if price_element:
        price = price_element.text.strip()
    else:
        price = "Price Not Found"
    
    product_titles.append(title)
    product_prices.append(price)
    product_urls.append(url)

driver.quit()

# Create DataFrame
df_scraped = pd.DataFrame({
    'title': product_titles,
    'price': product_prices,
    'url': product_urls
})

print(df_scraped)
# Save to CSV if needed
df_scraped.to_csv('amazon_scraped_data.csv', index=False)
