import pandas as pd

# Load the CSV file with datetime parsing
temp = pd.read_csv('/content/gdrive/MyDrive/SWE/river.csv', parse_dates=['datetime'])

# Set the datetime column as the index
temp.set_index('datetime', inplace=True)

# Convert the relevant column to numeric forcing errors to NaN
temp['211999_00060'] = pd.to_numeric(temp['211999_00060'], errors='coerce')

# Drop rows with NaN values in the numeric column
temp.dropna(subset=['211999_00060'], inplace=True)

# Resample to daily frequency and calculate the mean for the numeric column
river_daily = temp.resample('D').agg({'211999_00060': 'mean'})

# Save to a new CSV file
river_daily.to_csv('/content/gdrive/MyDrive/SWE/river_daily.csv')

# Display the resulting DataFrame
print(river_daily.head())
