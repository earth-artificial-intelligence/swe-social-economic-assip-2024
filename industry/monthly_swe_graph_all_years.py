import pandas as pd
import matplotlib.pyplot as plt

# Define the coordinate boundary for Washington
washington_bounds = {'lat_min': 45.5, 'lat_max': 49.0, 'lon_min': -124.9, 'lon_max': -116.9}

# Load the dataset
# Assuming the dataset is named 'swe_data.csv' and is in the same directory
df = pd.read_csv('cleaned_swe_2013_2024.csv')

# Filter the dataset for stations within Washington boundaries
washington_stations = df[
    (df['lat'] >= washington_bounds['lat_min']) & 
    (df['lat'] <= washington_bounds['lat_max']) & 
    (df['lon'] >= washington_bounds['lon_min']) & 
    (df['lon'] <= washington_bounds['lon_max'])
]

# Convert the date column to datetime
washington_stations['date'] = pd.to_datetime(washington_stations['date'])

# Extract the month and year from the date
washington_stations['year_month'] = washington_stations['date'].dt.to_period('M')

# Calculate the monthly mean SWE for Washington
monthly_mean_swe = washington_stations.groupby('year_month')['swe_value'].mean().reset_index()

# Convert year_month to datetime for plotting
monthly_mean_swe['year_month'] = monthly_mean_swe['year_month'].dt.to_timestamp()

# Plot the monthly mean SWE
plt.figure(figsize=(12, 6))
plt.plot(monthly_mean_swe['year_month'], monthly_mean_swe['swe_value'], marker='o')
plt.title('Monthly Mean SWE in Washington (2013-2023)')
plt.xlabel('Month')
plt.ylabel('Mean SWE (inches)')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
