import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from scipy.stats import pearsonr

# Load the datasets
snotel_data = pd.read_csv('cleaned_swe_2013_2024.csv')
food_prices = pd.read_csv('consumer_price_index.csv')

# Clean the SNOTEL dataset
snotel_data['date'] = pd.to_datetime(snotel_data['date'])
snotel_data['year'] = snotel_data['date'].dt.year

# Ensure numerical columns are of type float
snotel_data['swe_value'] = pd.to_numeric(snotel_data['swe_value'], errors='coerce')
food_prices['consumer_price_index'] = pd.to_numeric(food_prices['consumer_price_index'], errors='coerce')

# Drop rows with NaN values that might have been introduced
snotel_data = snotel_data.dropna(subset=['swe_value'])
food_prices = food_prices.dropna(subset=['consumer_price_index'])

# Aggregate SWE by year
yearly_swe = snotel_data.groupby('year')['swe_value'].mean().reset_index()
swe_counts_per_year = snotel_data.groupby('year')['swe_value'].count()

print(yearly_swe)
print("SWE COUNTS PER YEAR: ",swe_counts_per_year)

# Merge the datasets on year
merged_data = pd.merge(yearly_swe, food_prices, on='year')

# Ensure merged_data is clean
merged_data = merged_data.dropna()

# Correlation analysis
corr, _ = pearsonr(merged_data['swe_value'], merged_data['consumer_price_index'])
print(f'Correlation coefficient: {corr}')

# Linear regression analysis
X = merged_data[['swe_value']]
y = merged_data['consumer_price_index']
model = LinearRegression().fit(X, y)
r_squared = model.score(X, y)
print(f'R-squared: {r_squared}')
print(f'Intercept: {model.intercept_}, Coefficients: {model.coef_}')

# Create predictions for plotting
merged_data['predicted_consumer_price_index'] = model.predict(X)

# Plotting
plt.figure(figsize=(10, 6))
sns.scatterplot(x='swe_value', y='consumer_price_index', data=merged_data, label='Observed')
sns.lineplot(x='swe_value', y='predicted_consumer_price_index', data=merged_data, color='red', label='Fitted line')
plt.xlabel('Yearly Average SWE')
plt.ylabel('Yearly Consumer Price Index')
plt.title('Relationship between SWE and Consumer Price Index')
plt.legend()
plt.show()
