# Yahtzee Game Setup
import random # For random number functions

def roll_all_dice():
    """Roll the initial 6 dice at start of game"""
    mylist = [] # Setup a list to hold the rolls
    for x in range(0,5): # For Loop to make 6 rolls
        mylist.append(random.randint(1,6)) # Each roll gets random int 1 to 6
        print "Dice ", x+1, " is", mylist[x] # Print dice # and value

def keep_dice(*args):
    """ Get a list of dice that player wants to keep """
    inputlist=[] # Setup a list to hold the list
    for x in args:
        inputlist.append(args) # Go through all the arguments player entered
    print "You are keeping dice: ", inputlist
    return inputlist

def roll_single_dice():
    return random.randint(1,6)

if __name__ == '__main__':
    random.seed() # Set a seed for random number gen
    roll_all_dice() # Roll initial 6 dice at start of game

    a = raw_input("Which dice would you like to keep?")
    keeping = keep_dice(a) # Keeps the answer

