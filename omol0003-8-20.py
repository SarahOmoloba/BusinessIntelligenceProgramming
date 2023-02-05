# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 18:39:25 2022

@author: sarah
"""

import re

dateSentence= '''The date 042022 can be written as 04/20/2022 and April 20, 2022'''
months = [' ',
    'January','February','March','April','May','June',
    'July','August','September','October','November','December'
]

datePattern = re.compile('\d{2}[/.-]\d{2}[/.-]\d{4}|\w+\s+\d+, \d{4}|\d{2}\d{2}\d{2}')

def format_date01(month, day, year):
    #pattern01
    return f'{months[month]} {day}, {year}'

def format_date02(month, day, year):
    #pattern02
    return f'{month}/{day}/{year}'

def format_date03(month, day, year):
    #pattern03
    return f'{month}{day}{year[2:]}'

def formarted_date(date):
    if re.match('\d{2}\d{2}\d{2}', date):
        month = int(date[:2])
        day = int(date[2:4]) 
        year = int(date[2:])
        print(format_date01(month, day, year))
        print(format_date02(month, day, year))
    elif re.match('\d{2}[/.-]\d{2}[/.-]\d{4}', date):
        month, day, year = date.split('/')
        print(format_date01(int(month), day, year))
        print(format_date03(month, day, year))
    elif re.match('\w+\s+\d+, \d{4}', date):
        monthNum = '04'
        month, day, year = date.replace(',', '').split(' ')
        print(format_date02(monthNum, day, year))
        print(format_date03(monthNum, day, year))


for date in datePattern.findall(dateSentence):
    print(f'The date {date} has been transformed to:')
    transformedDate = formarted_date(date)
    print(transformedDate)