import pandas as pd
from statsmodels.stats.outliers_influence import variance_inflation_factor

X = sm.add_constant(merged_df[['swe', 'spatial_lag_swe']])
vif_data = pd.DataFrame()
vif_data['Variable'] = X.columns
vif_data['VIF'] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
print(vif_data)
