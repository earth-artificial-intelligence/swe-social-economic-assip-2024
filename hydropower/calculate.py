import pandas as pd

# Load the spreadsheet

def calc(year):
    file_path = f'WindGenTotalLoadYTD_{year}.xlsx'
    df = pd.read_excel(file_path) # , skiprows=23

    # Clean up the dataframe
    df.columns = df.iloc[0]
    df = df[1:]
    df = df.rename(columns={df.columns[0]: 'Date/Time', df.columns[6]: 'TOTAL HYDRO GENERATION (MW)'}) #rename the column so its easier

    # Convert 'TOTAL HYDRO GENERATION (MW)' to numeric
    df['TOTAL HYDRO GENERATION (MW)'] = pd.to_numeric(df['TOTAL HYDRO GENERATION (MW)'], errors='coerce')

    # Remove rows with NaN in 'TOTAL HYDRO GENERATION (MW)'
    df = df.dropna(subset=['TOTAL HYDRO GENERATION (MW)'])

    # Convert 'Date/Time' to datetime
    df['Date/Time'] = pd.to_datetime(df['Date/Time'])

    # Set 'Date/Time' as the index
    df.set_index('Date/Time', inplace=True)

    # Resample data to monthly and calculate the total MWh generated per month
    monthly_hydro_generation_mwh = df['TOTAL HYDRO GENERATION (MW)'].resample('M').sum() * (5/60)

    # Display the result
    print(monthly_hydro_generation_mwh)

    # Save the result to a new Excel file
    output_file_path = f'Monthly_Hydro_Generation_{year}.xlsx'
    monthly_hydro_generation_mwh.to_excel(output_file_path, sheet_name='Monthly Hydro Generation (MWh)')


calc(2022)
# don't skip rows starting 2022

# 2013,14,15,16 = skip 22 rows
# 2017 = skip 25 rows
#2018, 2019, 2020, 2021 =  skip 23 rows

# 6 (all .xls): 2013, 2014,2015, 2016,2017, 2018, 2019, 2020, 2021
# 12 (all .xlsx): 2022
