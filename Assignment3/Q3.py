import pandas as pd
from sklearn.preprocessing import MinMaxScaler, MaxAbsScaler, Normalizer, StandardScaler

df = pd.read_csv('apple_global_sales_dataset.csv')

num_cols = df.select_dtypes(include=['int64', 'float64']).columns
X = df[num_cols]

minmax = MinMaxScaler().fit_transform(X)
maxabs = MaxAbsScaler().fit_transform(X)
norm = Normalizer().fit_transform(X)
std = StandardScaler().fit_transform(X)

pd.DataFrame(minmax, columns=num_cols).to_csv('minmax.csv', index=False)
pd.DataFrame(maxabs, columns=num_cols).to_csv('maxabs.csv', index=False)
pd.DataFrame(norm, columns=num_cols).to_csv('normalized.csv', index=False)
pd.DataFrame(std, columns=num_cols).to_csv('standardized.csv', index=False)