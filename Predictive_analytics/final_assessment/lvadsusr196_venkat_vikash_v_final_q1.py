# -*- coding: utf-8 -*-
"""LVADSUSR196_Venkat_Vikash_V_final_Q1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-iJAJ64yBLSWnYM4nw6y0s6HgH9m8Pjn
"""

#IMPORTS FOR EVERYTHING
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.metrics import r2_score,mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import seaborn as sns

df = pd.read_csv("/content/Fare prediction.csv")

df.head()

df.info()

"""**CHECKING FOR NULL VALUES AND DUPLICATES**"""

df.isnull().sum()
#There are no null values

df.duplicated().sum()

"""**EDA**"""

plt.hist(df['fare_amount'])

sns.pairplot(df)

"""**CHECKING CORRELATION**"""

corr = df.corr(numeric_only = True)
sns.heatmap(corr,annot=True)

"""**OUTLIER HANDLING**"""

sns.boxplot(df[['fare_amount','passenger_count']])
# We could see there are potential outliers in the fare amount

#Handling outliers
df['fare_amount'] = df['fare_amount'].where(df['fare_amount']<180)

df.columns

#X = df[['pickup_longitude','pickup_latitude', 'dropoff_longitude', 'dropoff_latitude',
#       'passenger_count']]
X = df[['pickup_longitude','passenger_count']]
y = df['fare_amount'] #target variable

#SCALING
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
X = scaler.fit_transform(X)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=40)

# Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)

rmse = mean_squared_error(y_test, y_pred,squared=False)
print("Root Mean Squared Error:", rmse)

# Coefficients and intercept
print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)

r2_s = r2_score(y_test, y_pred)
print("R2 Score:", r2_s)