import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

# Create the CSV files based on the provided data

# Now read the data from the CSV files and generate the plot
def graph(year): 
    swe_df = pd.read_csv(f'{year}swe.csv')
    hydro_df = pd.read_csv(f'{year}hydro.csv')

    # Merge the dataframes on the 'year' column
    merged_df = pd.merge(swe_df, hydro_df, on='month')

    # Drop rows where power data is missing
    merged_df.dropna(subset=['power'], inplace=True)

    # Extract the relevant columns
    years = merged_df['month']
    swe_mean = merged_df['swe']
    hydro = merged_df['power']

    # Calculate the linear regression
    slope, intercept, r_value, p_value, std_err = linregress(swe_mean, hydro)

    # Create the scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(swe_mean, hydro, color='blue', label='Data points')

    # Plot the trend line
    trend_line = slope * swe_mean + intercept
    plt.plot(swe_mean, trend_line, color='red', label=f'Trend line (R²={r_value**2:.2f})')

    # Add labels and title
    plt.xlabel('SWE monthly Mean (Inches)')
    plt.ylabel('Monthly Hydro Power (millions of MWh)')
    plt.title(f'Correlation between SWE Mean and Hydropower {year}')
    plt.legend()

    # Show the plot
    plt.grid(True)
    plt.show()

graph(2022)