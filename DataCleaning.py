import pandas as pd

# Load the CSV file
file_path = 'nvre_properties.csv'
nvre_properties_df = pd.read_csv(file_path)

# Create a dictionary for specific replacements in the 'Borough' column
borough_replacements = {
    "City of London.": "City of London",
    # Add other replacements as needed
    "Westminster": "City of Westminster",
    "Hammersmith&Fulham": "Hammersmith and Fulham",
    "Richmond": "Richmond upon Thames",
    "Tower Hamlet": "Tower Hamlets"
    # Add more corrections here if necessary
}

# Apply the replacements
nvre_properties_df['Borough'] = nvre_properties_df['Borough'].replace(borough_replacements)

# Convert the '3 Bed Price' column to string, replace commas, and then check for non-numeric values
nvre_properties_df['3 Bed Price'] = nvre_properties_df['3 Bed Price'].astype(str).str.replace(',', '')

# Identify non-numeric values in the '3 Bed Price' column
non_numeric_mask = pd.to_numeric(nvre_properties_df['3 Bed Price'], errors='coerce').isna()

# Replace non-numeric values with empty strings
nvre_properties_df.loc[non_numeric_mask, '3 Bed Price'] = ''

# Save the cleaned data to a new CSV file
cleaned_file_path = 'cleaned_nvre_properties.csv'
nvre_properties_df.to_csv(cleaned_file_path, index=False)

print(f"Cleaned data saved to {cleaned_file_path}")
