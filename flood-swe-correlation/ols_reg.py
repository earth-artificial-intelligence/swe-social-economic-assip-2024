import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import statsmodels.api as sm

# Standardize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(merged_df[['swe', 'spatial_lag_swe']])

# Apply PCA
pca = PCA(n_components=1)  # Reduce to 1 component
X_pca = pca.fit_transform(X_scaled)

# Create a DataFrame with the principal component
merged_df['pca_component'] = X_pca

# Fit the model with PCA component
y = merged_df['river_flow']
X = sm.add_constant(merged_df[['pca_component']])

model = sm.OLS(y, X).fit()
print(model.summary())
