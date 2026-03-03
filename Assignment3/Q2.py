import pandas as pd
from sklearn.preprocessing import LabelEncoder, OrdinalEncoder

df = pd.read_csv('apple_global_sales_dataset.csv')

cat_cols = df.select_dtypes(include=['object']).columns

df_onehot = pd.get_dummies(df, columns=cat_cols)

df_label = df.copy()
le = LabelEncoder()
for col in cat_cols:
    df_label[col] = le.fit_transform(df_label[col])

df_ordinal = df.copy()
oe = OrdinalEncoder()
df_ordinal[cat_cols] = oe.fit_transform(df_ordinal[cat_cols])

df_freq = df.copy()
for col in cat_cols:
    freq = df_freq[col].value_counts()
    df_freq[col] = df_freq[col].map(freq)

target_col = df.columns[-1]
df_target = df.copy()
means = df_target.groupby(cat_cols[0])[target_col].mean()
df_target[cat_cols[0]] = df_target[cat_cols[0]].map(means)

df_onehot.to_csv('onehot.csv', index=False)
df_label.to_csv('label.csv', index=False)
df_ordinal.to_csv('ordinal.csv', index=False)
df_freq.to_csv('frequency.csv', index=False)
df_target.to_csv('target.csv', index=False)