import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Compute the correlation matrix
corr_matrix = merged_df[['swe', 'river_flow', 'spatial_lag_swe']].corr()

# Create a heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', vmin=-1, vmax=1)
plt.title('Correlation Matrix Heatmap')
plt.show()
