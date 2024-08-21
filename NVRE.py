import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Ensure GUI is off
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Choose Chrome Browser
driver = webdriver.Chrome(options=chrome_options)

# URL of the website to scrape
url = "https://nvre.co.uk/property"

# Open the URL
driver.get(url)

# Wait for the property listings to load
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "development_small_container"))
)

# Get the page source and parse it with BeautifulSoup
page_source = driver.page_source
soup = BeautifulSoup(page_source, 'html.parser')

# Find all property listings
properties = soup.find_all('div', class_='development_small_container')

# Extract details for each property
property_list = []

for property in properties:
    title_tag = property.find('h2')
    details_tag = property.find('div', class_='flex-container with_text')

    title = title_tag.text.strip() if title_tag else 'N/A'

    # Initialize variables
    price_studio = price_1bed = price_2bed = price_3bed = price_4bed = zone = postcode = borough = station = 'N/A'

    if details_tag:
        price_tags = details_tag.find_all('li')

        for li in price_tags:
            spans = li.find_all('span', class_='showLanguage', language='en')
            if not spans:
                continue  # Skip if no English text found

            text = li.get_text(separator=" ", strip=True)

            if 'Studio:' in text:
                price_studio = text.split('£')[-1].strip()
            elif '1 bed' in text:
                price_1bed = text.split('£')[-1].strip()
            elif '2 bed:' in text:
                price_2bed = text.split('£')[-1].strip()
            elif '3 bed:' in text:
                price_3bed = text.split('£')[-1].strip()
            elif '4 bed:' in text:
                price_4bed = text.split('£')[-1].strip()
            elif 'Zone:' in text:
                zone = text.split('：')[-1].strip()
            elif 'Postcode:' in text:
                postcode = text.split('：')[-1].strip()
            elif 'Borough:' in text:
                borough = text.split('：')[-1].strip()
            elif 'Station:' in text:
                station = text.split('：')[-1].strip()

    property_list.append({
        "Title": title,
        "Studio Price": price_studio,
        "1 Bed Price": price_1bed,
        "2 Bed Price": price_2bed,
        "3 Bed Price": price_3bed,
        "4 Bed Price": price_4bed,
        "Zone": zone,
        "Postcode": postcode,
        "Borough": borough,
        "Station": station,
    })

# Close the driver
driver.quit()

# Create a DataFrame from the list of properties
df = pd.DataFrame(property_list)

# Save the DataFrame to a CSV file
csv_file_path = "nvre_properties.csv"
df.to_csv(csv_file_path, index=False)

print(f"Data saved to {csv_file_path}")
