import pandas as pd
import matplotlib.pyplot as plt

def corr(year):
    # Load the CSV files
    hydro_data = pd.read_csv(f'{year}hydro.csv')
    swe_data = pd.read_csv(f'{year}swe.csv')

    # Merge the datasets on the month
    merged_data = pd.merge(hydro_data, swe_data, on='month')

    # Calculate the correlation between hydropower generated and SWE
    correlation = merged_data['power'].corr(merged_data['swe'])
    print(f'The correlation between total hydropower generated and mean SWE is: {correlation:.4f}')

    # Combined line plot
    fig, ax1 = plt.subplots(figsize=(12, 6))

    color = 'tab:blue'
    ax1.set_xlabel('Month')
    ax1.set_ylabel('Hydropower Generated (MWh)', color=color)
    ax1.plot(merged_data['month'], merged_data['power'], marker='o', color=color, label='Hydropower Generated (MWh)')
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()
    color = 'tab:orange'
    ax2.set_ylabel('Mean SWE (inches)', color=color)
    ax2.plot(merged_data['month'], merged_data['swe'], marker='s', color=color, label='Mean SWE (inches)')
    ax2.tick_params(axis='y', labelcolor=color)

    fig.tight_layout()
    plt.title(f'{year} Combined Trends of Hydropower Generated and SWE over Months')
    plt.grid(True)
    plt.show()


corr(2023)
