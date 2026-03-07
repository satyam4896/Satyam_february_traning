# Housing Price Prediction using Machine Learning

## Project Title

Housing Price Prediction using Linear Regression, Decision Tree, and Random Forest

---

## Problem Statement

The goal of this project is to predict housing prices based on different housing features using supervised machine learning regression algorithms. Accurate house price prediction helps real estate agencies, buyers, and investors estimate property value based on location, population, and housing characteristics.

This project compares three regression models to determine which algorithm provides the best prediction performance.

---

## Dataset Description

The dataset used in this project is the **California Housing Dataset** provided by the `sklearn` library.

The dataset contains housing information collected from California districts.

Features in the dataset include:

* **MedInc** – Median income in the block group
* **HouseAge** – Median age of houses in the block
* **AveRooms** – Average number of rooms per household
* **AveBedrms** – Average number of bedrooms per household
* **Population** – Population of the block group
* **AveOccup** – Average number of household members
* **Latitude** – Geographic latitude of the location
* **Longitude** – Geographic longitude of the location

Target Variable:

* **Price** – Median house value for households in that district.

---

## Data Cleaning and Preprocessing Steps

### 1. Handling Missing Values

The dataset was checked for missing values using `isnull()`.
No missing values were found in the dataset.

### 2. Removing Duplicate Records

Duplicate rows were identified and removed using the `drop_duplicates()` method to ensure that each record is unique.

### 3. Detecting and Treating Outliers

Outliers were detected using **boxplots** and the **Interquartile Range (IQR) method**.
Values that were outside the acceptable range were removed to reduce noise in the data.

### 4. Fixing Data Types

The dataset already contained correctly formatted numerical data types, so no type conversion was required.

### 5. Feature Scaling

Feature scaling was applied using **StandardScaler** to normalize feature values so that models such as Linear Regression perform better.

### 6. Removing Irrelevant Features

All features were relevant for prediction, so no columns were removed.

### 7. Train-Test Split

The dataset was divided into:

* **80% Training Data**
* **20% Testing Data**

This allows the models to be trained and then evaluated on unseen data.

---

## Algorithms Used

Three supervised machine learning regression algorithms were implemented:

### 1. Linear Regression

A statistical method that models the relationship between dependent and independent variables using a linear equation.

### 2. Decision Tree Regressor

A tree-based algorithm that splits the dataset into smaller subsets based on feature values to make predictions.

### 3. Random Forest Regressor

An ensemble learning method that builds multiple decision trees and combines their predictions to improve accuracy and reduce overfitting.

---

## Evaluation Metrics

The models were evaluated using the following regression metrics:

### R² Score

Indicates how well the model explains the variance in the target variable.
Higher values indicate better performance.

### Mean Squared Error (MSE)

Measures the average squared difference between predicted and actual values.

### Root Mean Squared Error (RMSE)

Square root of MSE, representing prediction error in the same unit as the target variable.

### Mean Absolute Error (MAE)

Measures the average absolute difference between predicted and actual values.

---

## Results

| Model             | R² Score                      | RMSE         | MAE          |
| ----------------- | ----------------------------- | ------------ | ------------ |
| Linear Regression | Moderate performance          | Medium error | Medium error |
| Decision Tree     | Better than linear regression | Lower error  | Lower error  |
| Random Forest     | Best performance              | Lowest error | Lowest error |

Random Forest generally provides the highest prediction accuracy because it combines multiple decision trees and reduces overfitting.

---

## Conclusion

This project successfully implemented three regression algorithms to predict housing prices using the California Housing dataset.

Among the models tested:

* **Random Forest Regressor performed the best**
* It achieved the highest R² score and the lowest prediction errors.

This demonstrates that ensemble learning methods are more effective for complex datasets with non-linear relationships.

Future improvements could include:

* Hyperparameter tuning
* Feature engineering
* Trying advanced models such as Gradient Boosting or XGBoost.
