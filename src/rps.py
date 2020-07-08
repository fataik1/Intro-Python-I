#write a program to play rock paper scissors with a user
#lets flesh out the rules and think about how this will work

#Rules: Rock ---> Scissors
    #   Scissors -> Paper
    #   Paper -> Rock

import random



# Flow:
# Start up program
# User will specify their choice
users_choice = input("Choose rock, paper, or scissors: ")

    #How does the program read the user's choice?
# Program also needs to specify its choice
possible_choices = ["rock", "paper", "scissors"]
programs_choice = random.choice(possible_choices)
    # How does the program determine its choice?
    # Just have it randomly pick a choice
    # Use Python's `random.choice` function
# Once both choices are made, compare them via the rules to
# see who won
if users_choice == "rock":
    if programs_choice == "rock":
        ties += 1
    elif programs_choice == "paper":
        #program won
    else:
        #user won
    
    #How do we do the comparsion?
    #use if statements
# Keep track of number of wins, losses, and ties for the user
    # How do we do this?
    # Have separate variables for each