# -*- coding: utf-8 -*-
"""LVADSUSR196_Venkat_Vikash_V_Q1_ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1hGE70OkpGEF1QsuwXFrYRDugsZ64JNuu

**MODEL IMPORT**
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import r2_score,mean_squared_error
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

df = pd.read_csv("/content/expenses.csv")

df.head()



"""**HANDLING MISSING VALUES AND OUTLIERS**"""

df.isnull().sum()
#There are null values in BMI

plt.hist(df['bmi'])

#Filling the data with median
median = df['bmi'].median()
df['bmi'] = df['bmi'].fillna(median)

#No null Values
df.isnull().sum()

#1 duplicate present
df.duplicated().sum()

#removing the duplicates
df = df.drop_duplicates()

"""**OUTLIER DETECTION**"""

#OUTLIER DETECTION

# Identify numerical columns by data type
numerical_columns = df.select_dtypes(include=['float64', 'int64']).columns

# Create a box plot for each numerical column
for column in numerical_columns:
    plt.figure(figsize=(10, 6))  # Set the figure size for better readability
    sns.boxplot(x=df[column])
    plt.title(f'Box Plot of {column}')
    plt.xlabel(column)
    plt.show()

#BI VARIATE AND CORRELATION
numerical_columns = df.select_dtypes(include=['float64', 'int64']).columns
# Compute the correlation matrix for numerical variables
correlation_matrix = df[numerical_columns].corr()
print("Correlation matrix:\n", correlation_matrix)

df.head()

"""**ONE HOT ENCODING**"""

#Encoded data
dummies = pd.get_dummies(df[['sex','smoker','region','charges','bmi','age']])

dummies.columns

correlation_matrix = dummies.corr()
sns.heatmap(correlation_matrix,annot=True)
#From the heatmap we could see that reigion is not highly correlated with charges

df['sex'].value_counts()

"""Since Gender is equally distributed we could drop them"""

encoded_df = dummies[['charges', 'bmi', 'age','smoker_no',
       'smoker_yes']]

encoded_df

X = encoded_df[['bmi', 'age','smoker_no','smoker_yes']]
y = encoded_df['charges']

#train test split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.3)

#Feature Scaling using MinMaxScaler
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = LinearRegression()
model.fit(X_train,y_train)
y_pred = model.predict(X_test)

y_pred

"""**EVALUVATION METRICS**"""

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)

rmse = mean_squared_error(y_test, y_pred,squared=False)
print("Root Mean Squared Error:", rmse)

print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)

r2_s = r2_score(y_test, y_pred)
print("R2 Score:", r2_s)