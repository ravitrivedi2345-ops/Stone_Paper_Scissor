import random

def get_computer_choice():
    choices = ['stone', 'paper', 'scissor']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'tie'

    if (user_choice == 'stone' and computer_choice == 'scissor') or \
       (user_choice == 'paper' and computer_choice == 'stone') or \
       (user_choice == 'scissor' and computer_choice == 'paper'):
        return 'user'
    
    return 'computer'
