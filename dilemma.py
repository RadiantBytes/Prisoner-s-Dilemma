#
# CS 224 Spring 2020 - After the Zombie Apocalypse
# Programming Assignment 4
#
# Simulates an automated game of the Prisoner's Dilemma
#   Certain game strategies are pre-programmed that can be
#   selected by the user to automatically use. The goal is
#   to generate more points than the opposing player 1.
#
# Author: Thomas Lynaugh
# Date: April 2, 2020
#

import sys
import time
import random

# Fetch an external class Player from player.py
from player import Player

def start_game(strategy_id, num_turns = 150):

    # setup game variables
    player1 = Player(0, 1)
    player2 = Player(0, strategy_id)

    curr_turn = 0

    #begin turns
    while curr_turn < num_turns:

        # interrigate player 1
        if (curr_turn == 0):
            interrigate(player1, curr_turn)
        else:
            interrigate(player1, curr_turn, player2.get_last_turn_action())

        # interrigate player 2
        if (curr_turn == 0):
            interrigate(player2, curr_turn)
        else:
            interrigate(player2, curr_turn, player1.get_last_turn_action())


        update_score(player1, player2)

        curr_turn += 1

    end_game(player1, player2)

def interrigate(prisoner, curr_turn = 0, opposing_last_action = 1):

    # Ignore last turn actions on the very first turn
    if (curr_turn > 0):
        prisoner.set_last_turn_action(prisoner.get_turn_action())


    # Confess or stay silent based on chosen game strategy

    # Tick-for-Tat
    if (prisoner.game_strat == 1):
        # If Prisoner 2 confessed last turn
        if (opposing_last_action == 1):
            prisoner.confess()

        # If Prisoner 2 was silent last turn
        elif (opposing_last_action == 0):
            prisoner.silent()

    # Always Confess
    elif (prisoner.game_strat == 2):
        prisoner.confess()

    # Always Stay Silent
    elif (prisoner.game_strat == 3):
        prisoner.silent()

    # Switch Each Turn
    elif (prisoner.game_strat == 4):
        if (prisoner.get_last_turn_action() == 0):
            prisoner.confess()
        else:
            prisoner.silent()

    # Choose Randomly
    else:
        if (random.randint(0,1) % 2 == 1):
            prisoner.confess()
        else:
            prisoner.silent()

def update_score(player1, player2):

    # If both prisoners were silent
    if ((player1.get_turn_action() == 0) & (player2.get_turn_action() == 0)):
        player1.add_points(1)
        player2.add_points(1)

    # If prisoner 1 confessed and prisoner 2 was silent
    elif ((player1.get_turn_action() == 1) & (player2.get_turn_action() == 0)):
        player1.add_points(5)

    # If prisoner 2 confessed and prisoner 1 was silent
    elif ((player1.get_turn_action() == 0) & (player2.get_turn_action() == 1)):
        player2.add_points(5)

    # If both prisoners confessed
    elif ((player1.get_turn_action() == 1) & (player2.get_turn_action() == 1)):
        player1.add_points(3)
        player2.add_points(3)

def end_game(player1, player2):
    print("\n Player 1 had " + str(player1.get_points()) + " points!\n")
    print("\n Player 2 had " + str(player2.get_points()) + " points!\n")

    if (player1.get_points() > player2.get_points()):
        print("Player 1 wins!")
    elif (player1.get_points() == player2.get_points()):
        print("Tie game!")
    else:
        print("Player 2 wins!")


def fetch_strat(strategy):
    # Match flag id to proper game strategy
    if (strategy == '1'):
        return "Tit-for-Tat"
    elif (strategy == '2'):
        return "Always Confess"
    elif (strategy == '3'):
        return "Always Stay Silent"
    elif (strategy == '4'):
        return "Switch Each Turn"
    elif (strategy == '5'):
        return "Choose Randomly"
    else:
        sys.exit("Issue determining strategy, please try again")

def print_strategy_info():
    print("--------------------------------------------------------------------------\n")
    print("# 1 - Tit-for-Tat\n")
    print("Choose whichever option the opposing player chose in the previous turn\n")
    print("# 2 - Always Confess\n")
    print("Choose to confess every turn\n")
    print("# 3 - Always Stay Silent\n")
    print("Choose to stay silent every turn\n")
    print("# 4 - Switch Each Turn\n")
    print("Switch choice every turn. Silence is chosen for the first turn.\n")
    print("# 5 - Choose Randomly\n")
    print("Randomly choose to stay silent or confess. Each has a 50% chance of occuring\n")
    print("\n--------------------------------------------------------------------------")

def main():

    print("Welcome to the Prisoner's Dilemma game\n\n")
    num_turns = input("Please type the desired number of turns : \n")
    print("\nGreat! The game will play for " + num_turns + " turns.\n")

    # User may use the 'info' flag, so break from prompt only when a valid flag has been selected by the user
    while True:
        strategy = input("What strategy will you use? Type 'info' for more information on the different strategies."
        + "Please type in the ID number of the strategy to use : \n\n")
        if (strategy.isdigit()):

            temp = input("You have chosen " + fetch_strat(strategy) + ", is this corrent? Type Y/N :\n")

            # Ensure no input shenanigans
            if temp.lower().replace(' ', '') == 'y':
                print("\n")
                break
            else:
                print("\n")
                continue;

        #Ensure no input shenanigans
        elif strategy.lower().replace(' ', '') == "info":
            print_strategy_info();

    print("\nStarting game with " + num_turns + " turns utilizing the strategy " + fetch_strat(strategy) + "...\n")

    # Simulate starting the game for extra immersion
    time.sleep(3)

    start_game(int(strategy), int(num_turns));

if __name__ == "__main__":
    main()
