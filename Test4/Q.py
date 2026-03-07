import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

housing = fetch_california_housing()

X = pd.DataFrame(housing.data, columns=housing.feature_names)
y = pd.Series(housing.target, name="Price")

df = pd.concat([X, y], axis=1)

print(df.head())
print(df.shape)
print(df.isnull().sum())

df = df.drop_duplicates()

plt.figure(figsize=(12,6))
sns.boxplot(data=df)
plt.xticks(rotation=90)
plt.show()

Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1

df = df[~((df < (Q1 - 1.5 * IQR)) | (df > (Q3 + 1.5 * IQR))).any(axis=1)]

X = df.drop("Price", axis=1)
y = df["Price"]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X = pd.DataFrame(X_scaled, columns=X.columns)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

lr = LinearRegression()
lr.fit(X_train, y_train)
y_pred_lr = lr.predict(X_test)

dt = DecisionTreeRegressor(random_state=42)
dt.fit(X_train, y_train)
y_pred_dt = dt.predict(X_test)

rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)
y_pred_rf = rf.predict(X_test)

def evaluate_model(y_test, y_pred, model_name):
    r2 = r2_score(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    mae = mean_absolute_error(y_test, y_pred)

    print("\n", model_name)
    print("R2 Score:", r2)
    print("MSE:", mse)
    print("RMSE:", rmse)
    print("MAE:", mae)

    return r2, mse, rmse, mae

lr_results = evaluate_model(y_test, y_pred_lr, "Linear Regression")
dt_results = evaluate_model(y_test, y_pred_dt, "Decision Tree")
rf_results = evaluate_model(y_test, y_pred_rf, "Random Forest")

results = pd.DataFrame({
    "Model": ["Linear Regression", "Decision Tree", "Random Forest"],
    "R2": [lr_results[0], dt_results[0], rf_results[0]],
    "MSE": [lr_results[1], dt_results[1], rf_results[1]],
    "RMSE": [lr_results[2], dt_results[2], rf_results[2]],
    "MAE": [lr_results[3], dt_results[3], rf_results[3]]
})

print(results)

plt.figure(figsize=(8,5))
sns.barplot(x="Model", y="R2", data=results)
plt.show()

plt.figure(figsize=(8,5))
sns.barplot(x="Model", y="RMSE", data=results)
plt.show()

best_model = results.sort_values(by="R2", ascending=False).iloc[0]
print("\nBest Model:")
print(best_model)