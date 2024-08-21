
# Property Scraper

This project is a web scraping tool designed to extract property listing details from the website [nvre.co.uk](https://nvre.co.uk/property) and save the extracted data into a CSV file. The tool utilizes Selenium, BeautifulSoup, and Pandas to automate the data extraction process and store the results in a structured format.

## Features

- Scrapes property listings, including title, prices for different types of accommodations (Studio, 1 Bed, 2 Bed, 3 Bed, 4 Bed), zone, postcode, borough, and nearby stations.
- Saves the extracted data into a CSV file named `nvre_properties.csv`.

## Requirements

- Python 3.x
- Google Chrome browser
- ChromeDriver (compatible with your Chrome browser version)

## Python Dependencies

Install the required Python packages using `pip`:

```bash
pip install selenium beautifulsoup4 pandas
```

## Setup

1. **Install ChromeDriver:**
   - Download ChromeDriver from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads) based on your Chrome browser version.
   - Ensure that the `chromedriver` binary is accessible from your `PATH`, or provide the path directly in the script.

2. **Clone or Download the Repository:**
   - Clone this repository or download the script file to your local machine.

3. **Running the Script:**
   - Open a terminal in the directory containing the script.
   - Run the script using Python:

   ```bash
   python property_scraper.py
   ```

## How It Works

1. **Selenium WebDriver Setup:**
   - The script configures Selenium to use Chrome in headless mode, meaning the browser won't open a visible window during execution.

2. **Navigating to the Website:**
   - The script navigates to the property listings page on the NVRE website.

3. **Waiting for Page Load:**
   - It waits until the property listings are fully loaded on the page.

4. **Scraping the Data:**
   - BeautifulSoup is used to parse the HTML and extract relevant data for each property listed.
   - The extracted details include property title, prices, zone, postcode, borough, and nearest station.

5. **Saving the Data:**
   - The scraped data is stored in a Pandas DataFrame, which is then saved as a CSV file (`nvre_properties.csv`).

6. **Script Completion:**
   - The script closes the browser and outputs the location of the saved CSV file.

## Example Output

After running the script, a CSV file named `nvre_properties.csv` will be created with the following structure:

| Title            | Studio Price | 1 Bed Price | 2 Bed Price | 3 Bed Price | 4 Bed Price | Zone | Postcode | Borough   | Station   |
|------------------|--------------|-------------|-------------|-------------|-------------|------|----------|-----------|-----------|
| Property Title 1 | £200,000      | £300,000    | £400,000    | £500,000    | £600,000    | 1    | NW1      | Camden    | Camden Town|
| Property Title 2 | £250,000      | £350,000    | £450,000    | £550,000    | £650,000    | 2    | SW1      | Westminster| Victoria  |

## Troubleshooting

- **WebDriverException:** If the script fails to initiate the ChromeDriver, ensure that the ChromeDriver path is correctly set and that it matches your installed Chrome version.
- **TimeoutException:** If the script times out while waiting for the page to load, consider increasing the wait time or checking your internet connection.
