from sklearn.linear_model import Ridge

# Prepare the data
X = merged_df[['swe', 'spatial_lag_swe']]
y = merged_df['river_flow']

# Apply Ridge Regression
ridge = Ridge(alpha=1.0)
ridge.fit(X, y)

# Print coefficients
print("Ridge coefficients:", ridge.coef_)
