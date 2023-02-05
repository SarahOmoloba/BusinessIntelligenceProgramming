import random
''' this code imports the random library for the shuffle function'''
def initializedeck():
# this function returns the randomized deck of cards    
    faces = ['Ace', 'Deuce', 'Three', 'Four', 'Five', 'six', 'Seven',
            'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King',]
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades',]
# the faces and suits variables are assigned their respective lists
    deck = []
# the variable deck is initialized
    for s in suits:
        for f in faces:
            decks = (f, s)
            deck.append(decks)
#creates and assigns the cards to deck   
    random.shuffle(deck)
    return deck
'''the shuffle function is applied and the result is returned to the 
initializedeck function'''
#    for card in deck:
 #       printcard = f'{card[0]} of {card[1]}'
#this code formats the cards 
    
#        print(f'{printcard:<25}', end = ' ')
    

formatted =initializedeck()
''' the initialized deck is returned to the formatted variable for ease of 
formatting'''
for l in range(len(formatted)):
    if (l+1) %4 != 0:
        
        print(f'{formatted[l][0]} of {formatted[l][1]:<10}', end = '\t')
       
    elif (l+1) %4 == 0:
        print(f'{formatted[l][0]} of {formatted[l][1]}',)
''' the codes above perform the iteration for the rows. '''