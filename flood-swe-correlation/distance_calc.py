import pandas as pd
import numpy as np
from math import radians, sin, cos, sqrt, atan2
import statsmodels.api as sm

def haversine(lon1, lat1, lon2, lat2):
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    r = 6371  # Radius of earth in kilometers
    return r * c

# Coordinates
lat_swe, lon_swe = 40.398035, -106.605171
lat_river, lon_river = 40.4816, -106.7769

# Calculate distance
distance_km = haversine(lon_swe, lat_swe, lon_river, lat_river)
print(f"Distance between locations: {distance_km:.2f} km")

# Assume a weight matrix where weight is inverse of distance
W = np.array([[1 / distance_km]])
print("Spatial Weight Matrix:\n", W)

# Add spatial lag: multiply SWE by the spatial weight matrix
merged_df['spatial_lag_swe'] = merged_df['swe'] * W[0, 0]
print("\nDataFrame with Spatial Lag:")
print(merged_df.head())

# Define the dependent variable (y) and independent variables (X)
y = merged_df['river_flow']
X = merged_df[['swe', 'spatial_lag_swe']]

# Add a constant to the independent variables
X = sm.add_constant(X)

# Fit the regression model
model = sm.OLS(y, X).fit()

# Print the regression results
print(model.summary())
