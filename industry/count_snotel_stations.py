import pandas as pd

# Load the CSV file
file_path = 'cleaned_swe_2013_2024.csv'
data = pd.read_csv(file_path)

# Extract unique latitude and longitude pairs
unique_coordinates = data[['lat', 'lon']].drop_duplicates()

# Count the number of unique coordinates
unique_count = unique_coordinates.shape[0]

print(f"The number of unique coordinates is: {unique_count}")
