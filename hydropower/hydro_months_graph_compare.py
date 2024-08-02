import pandas as pd
import matplotlib.pyplot as plt

def graph_comparison(year1, year2):
    # Read data from CSV
    data1 = pd.read_csv(f'{year1}hydro.csv')
    data2 = pd.read_csv(f'{year2}hydro.csv')

    # Plotting
    plt.figure(figsize=(10, 6))
    
    plt.plot(data1['month'], data1['power'], marker='o', label=f'{year1}')
    plt.plot(data2['month'], data2['power'], marker='o', label=f'{year2}')
    
    plt.title('Monthly Hydropower Generation in Washington State (MWh)')
    plt.xlabel('Month')
    plt.ylabel('Power Generated (Millions of MWh)')
    plt.xticks(data1['month'])
    plt.legend()
    plt.grid(True)
    plt.show()

# Compare the years 2022 and 2023
graph_comparison(2022, 2023)
