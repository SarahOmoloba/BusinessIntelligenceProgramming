import pandas as pd
# this imports the pandas library as pd to shorten it each time it's called
temp_dict ={'Maxine': [38, 37, 39], 'James': [36,35,36], 'Amanda': [37,36,35]}
# the tempratures dictionary is crated
tempratures = pd.DataFrame(temp_dict)
print(tempratures)
# it is then transformed into a data frame and outputed
tempratures.index = ['Morning', 'Afternoon', 'Evening']
#using the index format the data frame is 2nd modified 

# Tasks
print('\n The temprature readings for Maxine are: ')
print(tempratures['Maxine'])

print('\n The morning temprature row result is as follows: ')
print(tempratures.loc['Morning'])

print('\n The morning and evening temprature rows result is as follows:')
print(tempratures.loc[['Morning','Evening']])

print('\n The temprature columns for Amanda and Maxine result is as follows:')
print(tempratures[['Amanda','Maxine']])

print('\n The morning and afternoon temprature readings for Amanda & Maxine:')
print(tempratures.loc['Morning':'Afternoon',['Amanda','Maxine']])

print('\n The temprature description: ')
print(tempratures.describe())

print('\n Transposing the temprature data frame')
print(tempratures.T)

print('\n Sorting the columns in alphabetical order')
print(tempratures.sort_index(axis=1))
