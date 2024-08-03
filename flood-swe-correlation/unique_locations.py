import pandas as pd

swe = pd.read_csv('/content/gdrive/MyDrive/SWE/final_merged_data_3yrs_cleaned_v3.csv')

# Convert the date column to datetime format
swe['date'] = pd.to_datetime(swe['date'], errors='coerce')
swe.dropna(subset=['date'], inplace=True)  # Drop rows with invalid dates

# Set the 'date' column as the index
swe.set_index('date', inplace=True)

# Find the earliest and latest dates in the dataset
earliest_date = swe.index.min()
latest_date = swe.index.max()

# Print the date range
print(f"The dataset covers the period from {earliest_date} to {latest_date}.")

# Locations that the database covers
unique_locations = swe[['lat', 'lon']].drop_duplicates()
print(unique_locations)

print(swe.head())
