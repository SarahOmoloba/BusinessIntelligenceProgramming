# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 16:55:45 2022

@author: sarah
"""
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from sklearn.linear_model import ElasticNet, Lasso, Ridge
from sklearn.model_selection import KFold, cross_val_score

diabetes = load_diabetes()  # Bunch object 
print(diabetes.DESCR)

diabetes.data.shape
diabetes.target.shape
diabetes.feature_names

pd.set_option('display.precision', 4)  # 4 digit precision for floats

diabetes_df = pd.DataFrame(diabetes.data, 
                             columns=diabetes.feature_names)
diabetes_df['DiseasesProg'] = pd.Series(diabetes.target)
diabetes_df.head()  # peek at first 5 rows
diabetes_df.describe()

sample_df = diabetes_df.sample(frac=0.1, random_state=17)
sns.set_style('whitegrid')                                    
for feature in diabetes.feature_names:
    plt.figure(figsize=(8, 4.5))  # 8"-by-4.5" Figure
    sns.scatterplot(data=sample_df, x=feature, 
                    y='DiseasesProg', hue='DiseasesProg', 
                    palette='cool', legend=False)
    
X_train, X_test, y_train, y_test = train_test_split(
    diabetes.data, diabetes.target, random_state=11)
X_train.shape   
X_test.shape

linear_regression = LinearRegression()
linear_regression.fit(X=X_train, y=y_train)

for i, name in enumerate(diabetes.feature_names):
    print(f'{name:>10}: {linear_regression.coef_[i]}')  
linear_regression.intercept_

#testing the model
predicted = linear_regression.predict(X_test)
expected = y_test
predicted[:5]  # first 5 predictions
expected[:5]   # first five targets    

#visualize result
df = pd.DataFrame()
df['Expected'] = pd.Series(expected)
df['Predicted'] = pd.Series(predicted)
 
figure = plt.figure(figsize=(9, 9))

axes = sns.scatterplot(data=df, x='Expected', y='Predicted', 
    hue='Predicted', palette='cool', legend=False)

start = min(expected.min(), predicted.min())

end = max(expected.max(), predicted.max())

axes.set_xlim(start, end)

axes.set_ylim(start, end)

line = plt.plot([start, end], [start, end], 'k--')

#model metrics

metrics.r2_score(expected, predicted)
estimators = {
    'LinearRegression': linear_regression,
    'ElasticNet': ElasticNet(),
    'Lasso': Lasso(),
    'Ridge': Ridge()
}
for estimator_name, estimator_object in estimators.items():
    kfold = KFold(n_splits=10, random_state=11, shuffle=True)
    scores = cross_val_score(estimator=estimator_object, 
        X=diabetes.data, y=diabetes.target, cv=kfold,
        scoring='r2')
    print(f'{estimator_name:>16}: ' + 
          f'mean of r2 scores={scores.mean():.3f}')