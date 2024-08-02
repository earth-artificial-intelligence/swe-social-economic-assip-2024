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

# Extract the year and month from the date
washington_stations['year'] = washington_stations['date'].dt.year
washington_stations['month'] = washington_stations['date'].dt.month

# Function to plot the monthly mean SWE for a range of years
def plot_monthly_mean_swe_for_years(start_year, end_year):
    plt.figure(figsize=(12, 6))
    
    for year in range(start_year, end_year + 1):
        # Filter the data for the specific year
        year_data = washington_stations[washington_stations['year'] == year]
        
        # Calculate the monthly mean SWE for the specific year
        monthly_mean_swe_year = year_data.groupby('month')['swe_value'].mean().reset_index()
        
        # Plot the monthly mean SWE for the specific year
        plt.plot(monthly_mean_swe_year['month'], monthly_mean_swe_year['swe_value'], marker='o', label=f'{year}')
    
    plt.title(f'Monthly Mean SWE in Washington (2014-2023)')
    plt.xlabel('Month')
    plt.ylabel('Mean SWE (inches)')
    plt.xticks(range(1, 13))
    plt.grid(True)
    plt.legend(title='Year')
    plt.tight_layout()
    plt.show()

# Plot the monthly mean SWE for the years 2014-2023
plot_monthly_mean_swe_for_years(2014, 2023)
