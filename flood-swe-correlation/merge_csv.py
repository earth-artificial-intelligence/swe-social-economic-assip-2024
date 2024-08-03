import pandas as pd

# Reload SWE and River Flow datasets
swe = pd.read_csv('/content/gdrive/MyDrive/SWE/final_merged_data_3yrs_cleaned_v3.csv')
swe['date'] = pd.to_datetime(swe['date'], errors='coerce')
swe.dropna(subset=['date'], inplace=True)
swe.set_index('date', inplace=True)

river_daily = pd.read_csv('/content/gdrive/MyDrive/SWE/river_daily.csv')
river_daily['datetime'] = pd.to_datetime(river_daily['datetime'], errors='coerce')
river_daily.set_index('datetime', inplace=True)

# Ensure the index names are consistent
swe.index.name = 'datetime'
river_daily.index.name = 'datetime'

# Check date ranges
print("SWE DataFrame date range:", swe.index.min(), "to", swe.index.max())
print("River Flow DataFrame date range:", river_daily.index.min(), "to", river_daily.index.max())

# Filter both datasets to overlapping date range
start_date = max(swe.index.min(), river_daily.index.min())
end_date = min(swe.index.max(), river_daily.index.max())

# Remove duplicates if necessary
swe = swe.loc[~swe.index.duplicated(keep='first')]
river_daily = river_daily.loc[~river_daily.index.duplicated(keep='first')]

# Now apply the date range filtering
swe_location = swe.loc[start_date:end_date]
river_daily = river_daily.loc[start_date:end_date]

# Inspect column names
print("SWE DataFrame columns:", swe_location.columns)
print("River Flow DataFrame columns:", river_daily.columns)

# Rename columns for clarity
swe_location.rename(columns={'swe_value': 'swe'}, inplace=True)
river_daily.rename(columns={'211999_00060': 'river_flow'}, inplace=True)

# Merge the datasets on the datetime index
merged_df = pd.merge(swe_location, river_daily, left_index=True, right_index=True, how='inner')

# Drop rows with missing values in 'swe' and 'river_flow'
merged_df.dropna(subset=['swe', 'river_flow'], inplace=True)

# Print the merged DataFrame and check for missing values
print("Merged DataFrame shape:", merged_df.shape)
print("\nFirst few rows of merged DataFrame:")
print(merged_df.head())

print("\nMissing Values in Merged DataFrame:")
print(merged_df.isnull().sum())
