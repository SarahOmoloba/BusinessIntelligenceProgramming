# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 18:13:41 2022

@author: Omoloba Oluwatomiloba Sarah
id:      041052780
due:     10th December 2022
"""
'''Import the libraries'''
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#from sklearn import the following libraries
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from sklearn.linear_model import ElasticNet, Lasso, Ridge
from sklearn.model_selection import KFold, cross_val_score

'''Define the functions'''
def datasetSelectionError(chosenDataset):
    '''this allows the user to retype the correct value if a wrong one was entered'''    
    print('That was not an option')
    try:
        chosenDataset = int(input('Retype the number you would like to work with'))
        print(f'Your number is {chosenDataset}, you are on the right track')
    except ValueError:
        print('please enter 1 for california & 2 for diabetes')
    except TypeError:
        print('no alphabeth allowed,enter 1 or 2')    
    
    return

#def valueErrorMessage():
    
#    return

def pauseExit():
    '''to allow the user to choose between exiting the program or continuing'''
    try:
        progressChosen = input('Do you want to continue or exit? y/n:')
        if progressChosen.lower() == 'n':
            exit()
    except ValueError:
        print('please enter y for continue & n for exit')
    except TypeError:
        print('no numerals allowed, y/n')
    return

def emptyLine():
    '''prints an empty line to tidy up the code'''
    print (' ')
    return

def coinToss():
    '''lets the user choose to view either the dataset's head or tail'''
    try:
        displayFace = input('Choose h for 1st 5 rows or t for last five rows')
        if displayFace.lower() == 'h':
            emptyLine()
            print(workingDataset_df.head())  # peek at first 5 rows
        elif displayFace.lower() == 't':
            emptyLine()
            print(workingDataset_df.tail()) # peek at last 5 rows
    except ValueError:
        print('please enter h for 1st 5 rows & t for last five rows ')
    except TypeError:
        print('no numerals allowed, h/t')   
    return

'''Load the datasets'''
#assign the datasets to a dictionary and print the list

theDataSetDict = {1: 'California', 2: 'Diabetes',}
datasetList = theDataSetDict.items()
print(datasetList)

#allow the user to select their dataset
chosenDataset = int(input('What number would you like to work with?'))
while chosenDataset in datasetList:
    try:        
        selectedDataset = datasetList.value()
        print(f'Great! you have chosen: {selectedDataset}')

    except:   
        datasetSelectionError()
    
#load the dataset from sklearn
if chosenDataset == 1:
    from sklearn.datasets import fetch_california_housing
    workingDataset = fetch_california_housing
elif chosenDataset == 2:
    from sklearn.datasets import load_diabetes
    workingDataset = load_diabetes
  
print(workingDataset.DESCR)

#ask the user if they would like to continue or exit
pauseExit()

#display the data shape, target shape and feature names

displayDataShape  = workingDataset.data.shape
displayTarShape   = workingDataset.target.shape
displayFeatName   = workingDataset.feature_names


print(f'The target shape is {displayTarShape}')
emptyLine()
print(f'The data has a total of {displayDataShape[0]} and {displayDataShape[1]} columns')
emptyLine()
print(f'The feature names as as follows: {displayFeatName}')
emptyLine()
pauseExit()
emptyLine()


'''Explore the data with pandas and visualize the features'''
# assign the data to a data frame
pd.set_option('display.precision', 4)  # 4 digit precision for floats

workingDataset_df = pd.DataFrame(workingDataset.data, 
                             columns=workingDataset.feature_names)

#define the target values
if  len(workingDataset.feature_names) == 8: # if user chose california dataset
    workingDataset['MedHouseValue'] = pd.Series(workingDataset.target)
    #lets the user choose to view either the dataset's head or tail
    coinToss()
    emptyLine()
    workingDataset_df.describe()
    
    sample_df = workingDataset_df.sample(frac=0.1, random_state=17)
#visualing the features
    sns.set_style('whitegrid')                                    
    for feature in workingDataset.feature_names:
        plt.figure(figsize=(8, 4.5))  # 8"-by-4.5" Figure
        sns.scatterplot(data=sample_df, x=feature, 
                      y='MedHouseValue', hue='MedHouseValue', 
                      palette='cool', legend=False)

elif len(workingDataset.feature_names) == 10: # if user chose diabetes dataset   
    workingDataset_df['DiseasesProg'] = pd.Series(workingDataset.target)
    #lets the user choose to view either the dataset's head or tail
    coinToss()
    emptyLine()
    workingDataset_df.describe()
    
    sample_df = workingDataset_df.sample(frac=0.1, random_state=17)
#visualing the features    
    sns.set_style('whitegrid')                                    
    for feature in workingDataset.feature_names:
        plt.figure(figsize=(8, 4.5))  # 8"-by-4.5" Figure
        sns.scatterplot(data=sample_df, x=feature, 
                      y='DiseasesProg', hue='DiseasesProg', 
                      palette='cool', legend=False)
        
#ask the user if they would like to continue or exit
pauseExit()

'''Split the dataset into training and testing data'''
#notify the user that the data will be split 
print('The data frame will now be split into training set and test set')
emptyLine()
X_train, X_test, y_train, y_test = train_test_split(
    workingDataset.data, workingDataset.target, random_state=11)
X_train.shape   
X_test.shape
#notify the user that the data has been splitted 
print('The spliting is complete')
emptyLine()


'''Train the data model'''

#notify the user that the model will now be trained

print('The model is being trained')
emptyLine()

linear_regression = LinearRegression()
linear_regression.fit(X=X_train, y=y_train)

for i, name in enumerate(workingDataset.feature_names):
    print(f'{name:>10}: {linear_regression.coef_[i]}')  
theIntercept = linear_regression.intercept_
emptyLine()
print(f'This is the intercept {theIntercept}')
emptyLine()
#notify the user that the model has now been trained
print('The training of the model is complete')
emptyLine()

pauseExit()
emptyLine()

'''Test the data model'''
#notify the user that the model will now be tested
print('The model is being tested')
emptyLine()

predicted = linear_regression.predict(X_test)
expected = y_test
predicted[:5]  # first 5 predictions
expected[:5]   # first five targets 

#notify the user that the model has now been tested
print('The testing of the model is complete, see the graph below')
emptyLine()

pauseExit()

'''Visualize the expected vs the predicted'''
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


'''Create the regression model'''

metrics.r2_score(expected, predicted)
estimators = {
    'LinearRegression': linear_regression,
    'ElasticNet': ElasticNet(),
    'Lasso': Lasso(),
    'Ridge': Ridge()
}
print('Only 1 step left!')
emptyLine()
pauseExit()
emptyLine()
for estimator_name, estimator_object in estimators.items():
    kfold = KFold(n_splits=10, random_state=11, shuffle=True)
    scores = cross_val_score(estimator=estimator_object, 
        X= workingDataset.data, y= workingDataset.target, cv=kfold,
        scoring='r2')
    
    print(f'{estimator_name:>16}: ' + 
          f'mean of r2 scores={scores.mean():.3f}')
    
    