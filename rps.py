# File: rps.py
# Description: Rock, Paper, Scissors Game, User VS Computer
import random
import time

def game ():
    '''
    Main function: Where data will be entered and seed will be selected.
    Input: name(string)|rounds(int)|seed_condicial(string)|seed_number(int)
    '''
    print("Welcome to ROCK PAPER SCISSORS. I, Computer, will be your opponent.")   
    name = input("Please enter your name: ") 
    print("Thank you!\n")
    rounds = int(input("Please enter the number of rounds to play:"))
    print("Thank you!\n")
    seed_condicional = input("Please enter y if you want to set the seed: ")
    if seed_condicional == "y":
        seed_number = int(input("Please enter an integer for the seed: "))
        random.seed(seed_number)
        print("Thank you!\n")
    elif seed_condicional == "n":
        print("A random seed will be selected\nThank you!\n")
        random.seed(time.time())# Use epochtime as a seed_number so never is going to be the same
    else:
        print("Wrong input value, try again")
        exit()
    sum_of_points = play_rounds(name, rounds)
    results(name,rounds,sum_of_points)

def get_computer_play():
    '''
    Generate ramdom number between 1 and 3, then that number will be replace by a string depends on dic_replace_values
    Output: computer_play(string)
    '''
    computer_play = str(random.randint(1, 3))
    computer_play = replace_inputs(computer_play)
    return computer_play

def replace_inputs (input_value):
    '''
    Replaces computer and player input values to have standardized data
    Input: input_value(string)
    Output: input_value(string)   
    '''   
    dic_replace_values = {"1": "R", "2": "P", "3": "S", "R": "Rock", "P": "Paper", "S": "Scissors"}
    for i, j in dic_replace_values.items():
        input_value = input_value.replace(i, j)
    return input_value

def game_rules (user_play,computer_play):
    '''
    Depending on the values of the computer and the player we will obtain a result following the rules of the game. 
    The results in favor of the player will give him a point that at the end will be added to a total score.
    Input: user_play(string)|computer_play(string)
    Output: point(int)
    '''   
    if user_play == computer_play:
        print("We picked the same thing. Round is a draw.")
        return 0
    elif (user_play == "Rock") and (computer_play == "Paper"):
        print("Paper covers Rock. I win.")
        return 0
    elif (user_play == "Rock") and (computer_play == "Scissors"):
        print("Rock breaks Scissors. You win.")
        return 1
    elif (user_play == "Paper") and (computer_play == "Rock"):
        print("Paper covers Rock. You win.")
        return 1
    elif (user_play == "Paper") and (computer_play == "Scissors"):
        print("Scissors cut Paper. I win.")
        return 0
    elif (user_play == "Scissors") and (computer_play == "Rock"):
        print("Rock breaks Scissors. I win.")
        return 0
    elif (user_play == "Scissors") and (computer_play == "Paper"):
        print("Scissors cut Paper. You win.")
        return 1

def play_rounds (name,rounds):
    '''
    A for loop is used to play the number of rounds input by the player.
    Input: name(string)|rounds(int)
    Output: sum of points(int)
    '''
    counter_points = []
    for i in range (1,rounds+1):
        user_play = input(f"\n{name}, enter your choice for this round.\nR for Rock, P for Paper, S for Scissors:") 
        user_play = replace_inputs (user_play)
        computer_play = get_computer_play()
        print(f"I pick {computer_play}.")
        points = game_rules (user_play,computer_play)
        counter_points.append(points)
    return sum(counter_points)

def results (name,rounds,wins):
    '''
    Print the score of the rounds.
    Input: name(string)|rounds(int)|wins(int)
    '''
    if rounds == 1: 
        print(f"\nWe played 1 round of ROCK PAPER SCISSORS.\n{name} won {wins} round.\nWell played.")
    if rounds > 1:
        print(f"\nWe played {rounds} rounds of ROCK PAPER SCISSORS.\n{name} won {wins} rounds.\nWell played.")










game()