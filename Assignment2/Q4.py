import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

df = pd.read_csv('apple_global_sales_dataset.csv')

num_cols = df.select_dtypes(include=['int64', 'float64']).columns

for col in num_cols:
    df[col] = np.log1p(df[col])

target_col = df.columns[-1]

X = df.drop(target_col, axis=1)
y = df[target_col]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

X_train.to_csv('X_train.csv', index=False)
X_test.to_csv('X_test.csv', index=False)
y_train.to_csv('y_train.csv', index=False)
y_test.to_csv('y_test.csv', index=False)