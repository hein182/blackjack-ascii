import os
import random
import random
import time
import sys

#global vars

wins = 0
losses = 0

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

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


#essential functions

def check_jqka(x):
    match x:
        case 1:
            return "ace"
        case 11:
            return "jack"
        case 12:
            return "queen"
        case 13:
            return "king"
        case _:
            return str(x)

#l, r = deck[1]
cur_card = 0
random.shuffle(deck)
d_hand = []
p_hand = []

def init_bj():
    global cur_card
    random.shuffle(deck)
    global d_hand
    global p_hand
    cur_card = 0
    d_hand = []
    p_hand = []

def format_card(x):
    l, r = deck[x]
    return check_jqka(l) + " of " + r

def print_slow(s):
    for letter in s:
        sys.stdout.write(letter)
        sys.stdout.flush()
        if letter == " ":
            time.sleep(random.randint(50,60)/1000)
            continue
        time.sleep(random.randint(60,74)/1000)  # Adjust sleep duration as needed for desired speed
    print("")

def draw_card(p, turn):
    global cur_card
    name = "themself"
    if turn == 'p':
        name = "you"
        words = f"{bcolors.OKGREEN}Dealer gives {name}:      " + format_card(cur_card) + "." + bcolors.ENDC
        print_slow(words)
    else:
        words0 = f"{bcolors.OKBLUE}Dealer gives {name}: " + format_card(cur_card) + "." + bcolors.ENDC
        print_slow(words0)
    p.append(deck[cur_card])
    cur_card += 1
    time.sleep(0.1)
def check_hand(p):
    values = []
    total = 0
    for c in p:
        l, r = c
        values.append(l)
    for value in values:
        if value == 1:
            total += 11
            continue
        if value >= 11:
            total += 10
            continue
        total += value
    if total > 21 and 1 in values:
        total = 0
        for value in values:
            if value >= 11:
                total += 10
                continue
            total += value
    return total

def win():
    global wins
    wins += 1
    print(f"       {bcolors.BOLD}{bcolors.OKCYAN}You win!{bcolors.ENDC}")
    print("Play again (y/n): ", end='')
    yn = input()
    if(yn == "y"):
        init_bj()
        blackJack()
    else:
        exit()

def draw():
    print(f"       {bcolors.UNDERLINE}You draw!{bcolors.ENDC}")
    print("Play again (y/n): ", end='')
    yn = input()
    if(yn == "y"):
        init_bj()
        blackJack()
    else:
        exit()


def lose():
    global losses
    losses += 1
    print(f"       {bcolors.WARNING}You lose!{bcolors.ENDC}")
    print("Play again (y/n): ", end='')
    yn = input()
    if(yn == "y"):
        init_bj()
        blackJack()
    else:
        exit()

def ask_hit():
    print("Dealer asks you for hit (y/n):", end='')
    yn = input()
    if yn == "y":
        draw_card(p_hand, 'p')
        if check_hand(p_hand) == 21:
            win()
        if check_hand(p_hand) > 21:
            print("You bust better luck next time.")
            lose()
    else:
        return 0 

def blackJack():
    d_stay = False
    d_bust = False
    p_stay = False
    os.system("clear")
    print(f"{bcolors.BOLD}       BlackJack (wins:{wins} losses:{losses}){bcolors.ENDC}")
    draw_card(p_hand, 'p')
    draw_card(d_hand, 'd')
    draw_card(p_hand, 'p')
    #check if win
    #print("current p_hand: " + str(check_hand(p_hand)))
    if check_hand(p_hand) == 21:
        win()
    a = ask_hit()
    if a == 0:
        p_stay = True
    draw_card(d_hand, 'd')
    if check_hand(d_hand) >= 17:
        d_stay = True
    if not p_stay:
        b = ask_hit()
        if b == 0:
            p_stay = True
    if not d_stay:
        draw_card(d_hand, 'd')
        if check_hand(d_hand) >= 17:
            d_stay = True
    if check_hand(d_hand) > 21:
        print("Dealer busts!")
        win()
    if not p_stay:
        c = ask_hit()
        if check_hand(p_hand) > 21:
            lose()
        if c != 0: # player drew 5 cards auto win
            win()
    while d_stay == False:
        if not d_stay:
            draw_card(d_hand, 'd')
            if check_hand(d_hand) >= 17:
                d_stay = True
            if check_hand(d_hand) > 21:
                print("Dealer busts!")
                win()
    #do last
    if check_hand(d_hand) > check_hand(p_hand):
        lose()
    if check_hand(d_hand) == check_hand(p_hand):
        draw()
    win()
init_bj()
blackJack()

