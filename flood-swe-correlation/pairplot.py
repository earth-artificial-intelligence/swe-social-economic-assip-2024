import seaborn as sns
import matplotlib.pyplot as plt

# Create a pair plot
sns.pairplot(merged_df[['swe', 'river_flow', 'spatial_lag_swe']])
plt.suptitle('Pair Plot of SWE, River Flow, and Spatial Lag SWE', y=1.02)
plt.show()
