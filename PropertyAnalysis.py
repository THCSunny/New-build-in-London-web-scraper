import pandas as pd
import numpy as np

# Load the cleaned CSV file
file_path = 'cleaned_nvre_properties.csv'
cleaned_nvre_properties_df = pd.read_csv(file_path)

# Specify the price columns
price_columns = ['Studio Price', '1 Bed Price', '2 Bed Price', '3 Bed Price', '4 Bed Price']

# Convert the price columns to numeric, replacing non-numeric values with NaN
for col in price_columns:
    cleaned_nvre_properties_df[col] = pd.to_numeric(cleaned_nvre_properties_df[col].astype(str).str.replace(',', ''),
                                                    errors='coerce')


# Define a function to format the prices
def format_currency(x):
    return f"£{x:,.2f}" if pd.notnull(x) else "N/A"


# Vectorize the formatting function
vectorized_format_currency = np.vectorize(format_currency)

# Calculate mean, mode, and median for each price column
summary_stats = {}
for col in price_columns:
    mean_val = cleaned_nvre_properties_df[col].mean()
    median_val = cleaned_nvre_properties_df[col].median()
    mode_val = cleaned_nvre_properties_df[col].mode()

    # Since mode can return multiple values, we handle it accordingly
    if not mode_val.empty:
        mode_val = mode_val.iloc[0]
    else:
        mode_val = np.nan

    summary_stats[col] = {
        'Mean': format_currency(mean_val),
        'Median': format_currency(median_val),
        'Mode': format_currency(mode_val)
    }

# Formatting the average prices by zone
average_prices_by_zone_cleaned = cleaned_nvre_properties_df.groupby('Zone')[price_columns].mean()
average_prices_by_zone_cleaned_readable = average_prices_by_zone_cleaned.apply(vectorized_format_currency)

# Formatting the average prices by borough
average_prices_by_borough_cleaned = cleaned_nvre_properties_df.groupby('Borough')[price_columns].mean()
average_prices_by_borough_cleaned_readable = average_prices_by_borough_cleaned.apply(vectorized_format_currency)

# Identify columns with missing data and quantify the missing values
missing_data_cleaned = cleaned_nvre_properties_df.isnull().sum()
missing_data_cleaned_readable = missing_data_cleaned.apply(lambda x: f"{x} missing values")

# Prepare the summary statistics for each price column
summary_stats_content = "\n".join([f"{col}: {stats}" for col, stats in summary_stats.items()])

# Prepare the results for output to a file
report_content = f"""
### Summary Statistics for Each Type of Apartment
{summary_stats_content}

### Average Prices by Zone
{average_prices_by_zone_cleaned_readable.to_string()}

### Average Prices by Borough (selected examples)
{average_prices_by_borough_cleaned_readable.head(10).to_string()}  # limiting to first 10 for brevity

### Missing Data
{missing_data_cleaned_readable.to_string()}
"""

# Define the file path
report_file_path = 'cleaned_property_report.txt'

# Write the report to a file
with open(report_file_path, 'w') as file:
    file.write(report_content)

print(f"Report saved to {report_file_path}")
