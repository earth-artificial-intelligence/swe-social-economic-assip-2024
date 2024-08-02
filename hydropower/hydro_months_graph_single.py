import pandas as pd
import matplotlib.pyplot as plt


def graph(year):
    # Read data from CSV
    data = pd.read_csv(f'{year}hydro.csv')

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(data['month'], data['power'], marker='o')
    plt.title(f'{year} Monthly Hydropower Generation in Washington State (MWh)')
    plt.xlabel('Month')
    plt.ylabel('Power Generated (MWh)')
    plt.xticks(data['month'])
    plt.grid(True)
    plt.show()


graph(2022)