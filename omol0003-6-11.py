# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 15:29:09 2022

@author: sarah
"""

import random

def roll_dice():
    """Roll two dice and return their face values as a tuple."""
    die1 = random.randrange(1, 7)
    die2 = random.randrange(1, 7)
    return (die1, die2)  # pack die face values into a tuple

def display_dice(dice):
    """Display one roll of the two dice."""
    die1, die2 = dice  # unpack the tuple into variables die1 and die2
    sum(dice)

            
#temp_table = []  
win_roll   ={}
lose_roll  ={}

for play in range(1,1000001):
    wincount       = 0
    losecount      = 0
    rolls          = 0

    die_values = roll_dice()
    rolls += 1  # first roll
    display_dice(die_values)
    

# determine game status and point, based on first roll
    sum_of_dice = sum(die_values)
    if sum_of_dice in (7, 11):
        game_status = 'WON'
#if the player wins, 1 is added to the win dictionary if the key already exist
#else a new key for the number of rolls and the 1 for the value is added        
        if rolls in win_roll.keys():
            wincount += 1
            win_roll[rolls] += 1
        else :
            wincount += 1
            win_roll.update({rolls: wincount})
            
    elif sum_of_dice in (2, 3, 12):  # lose
        game_status = 'LOST'
#the same as the win applies for the loss dictionary if the player looses        
        if rolls in lose_roll.keys():
            losecount += 1
            lose_roll[rolls] +=1
        else :
            losecount += 1
            lose_roll.update({rolls: losecount}) 
    else:  # remember point
        game_status = 'CONTINUE'
        my_point = sum_of_dice

# continue rolling until player wins or loses
    while game_status == 'CONTINUE':
        die_values = roll_dice()
        display_dice(die_values)
        sum_of_dice = sum(die_values)
        rolls +=1 #to keep track of the number of rolls it takes for resolution

        if sum_of_dice == my_point:  # win by making point
            game_status = 'WON'
            if rolls in win_roll.keys():
                wincount + 1
                win_roll[rolls] += 1
            else :
                wincount += 1
                win_roll.update({rolls: wincount})
                
        elif sum_of_dice == 7:  # lose by rolling 7
            game_status = 'LOST'
            if rolls in lose_roll.keys():
                losecount + 1
                lose_roll[rolls] += 1
            else :
                losecount += 1
                lose_roll.update({rolls: losecount}) 

#get the percentage of the wins and losses over the million game plays                
win_dict_sum = sum(win_roll.values())
lose_dict_sum = sum(lose_roll.values())

wins_per_total =   ( win_dict_sum / 1000000) * 100
lose_per_total =   ( lose_dict_sum / 1000000) * 100          

#a new dictionary is created to keep track of the total percentage of the wins
#and losses per roll
resolved_dict = {
    key: win_roll.get(key, 0) + lose_roll.get(key, 0) for key in set(win_roll) | set(lose_roll)
}

#the result outputs
print(f'Percentage of Wins: {wins_per_total:.2f}%')    
print(f'Percentage of Losses: {lose_per_total:.2f}%') 
print('Percentage of Wins/Losses based on the total number of rolls') 
print('     ')
print('          %Resolved       Cummulative%')
print('Rolls    on this roll      of Resolved')

cumulative_final = 0
for r, v in resolved_dict.items():
    resolved_percent = ( v / 1000000) * 100 
    cumulative_final +=resolved_percent

        
        
    print(f'{r:<5}{format(resolved_percent,".2f"):>15}% {format(cumulative_final,".2f"):>15}%')


