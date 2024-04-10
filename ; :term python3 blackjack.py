import os
import random

#create the deck
deck = []

for x in range(0, 4 * 13):
    deck.append(0)

suits = ["hearts", "spades", "clubs", "diamonds"]

for y in range(0, 4):
    for x in range(0, 13):
        index = y * 13 + x
        deck[index] = (x + 1, suits[y])  # Adding 1 to x to represent ranks from 1 to 13

#end of deck creation

random.shuffle(deck)

#essential functions

def check_jqka(x):
    match x:
        case 11:
            return "jack"
        case 12:
            return "queen"
        case 13:
            return "king"
        case _:
            return x

print(deck)
