#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 09:50:00 2019

@author: yutongzhang
"""

import pandas as pd
from sklearn import linear_model
import statsmodels.api as sm

data = pd.read_csv("winequality-red.csv")

import matplotlib.pyplot as plt
plt.scatter(data["citric acid"], data["quality"], color = "red")
plt.title('Quality Vs Citric Acid Level', fontsize=14)
plt.xlabel('Citric Acid Level', fontsize=14)
plt.ylabel('Quality', fontsize=14)
plt.grid(True)
plt.show()

plt.scatter(data['pH'], data['quality'], color='green')
plt.title('Quality Vs pH', fontsize=14)
plt.xlabel('pH', fontsize=14)
plt.ylabel('Quality', fontsize=14)
plt.grid(True)
plt.show()

X = data[['pH','citric acid', "fixed acidity", "volatile acidity", "residual sugar", "chlorides", "free sulfur dioxide", "total sulfur dioxide", "density", "sulphates", "alcohol"]]
Y = data['quality']


# with sklearn
regr = linear_model.LinearRegression()
regr.fit(X, Y)

print('Intercept: \n', regr.intercept_)
print('Coefficients: \n', regr.coef_)


# prediction with sklearn
New_PH = 3.0
New_Citric_Acid = 0.5
New_fixed_acidity = 8
new_volatile_acidity = 0.7
new_residual_sugar = 2
new_chlorides = 0.08
new_free_sulfur_dioxide = 17
new_total_sulfur_dioxide = 60
new_density = 0.9978
new_sulphates = 3.65
new_alcohol = 0.58
print ('Predicted Quality: \n', regr.predict([[New_PH , New_Citric_Acid,New_fixed_acidity,new_volatile_acidity,new_residual_sugar,new_chlorides,new_free_sulfur_dioxide,new_total_sulfur_dioxide,new_density,new_sulphates,new_alcohol]]))


# with statsmodels
X = sm.add_constant(X) # adding a constant
 
model = sm.OLS(Y, X).fit()
predictions = model.predict(X) 
 
print_model = model.summary()
print(print_model)

from scipy import stats
import numpy as np
z = np.abs(stats.zscore(data))


data_outlier = data[(z < 0.8).all(axis=1)]
print(data_outlier)

