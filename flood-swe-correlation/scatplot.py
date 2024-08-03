import seaborn as sns
import matplotlib.pyplot as plt

# Scatter plot of SWE vs River Flow with regression line
plt.figure(figsize=(8, 6))
sns.regplot(x='swe', y='river_flow', data=merged_df, line_kws={"color":"red"})
plt.title('SWE vs River Flow')
plt.xlabel('SWE')
plt.ylabel('River Flow')
plt.show()

# Scatter plot of Spatial Lag SWE vs River Flow with regression line
plt.figure(figsize=(8, 6))
sns.regplot(x='spatial_lag_swe', y='river_flow', data=merged_df, line_kws={"color":"red"})
plt.title('Spatial Lag SWE vs River Flow')
plt.xlabel('Spatial Lag SWE')
plt.ylabel('River Flow')
plt.show()
