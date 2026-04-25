import random
from players import players_list

def display_intro():
    print("Welcome to MLB Guessing Game!")
    print("Try to guess the mystery MLB player.")
    print("You will get hints after each incorrect guess.")
    print()

def find_player(guess):
    for player in players_list:
        if player["name"].lower() == guess.lower():
            return player
    return None

def hints(guess_player, mystery_player):
    print("\nFeedback:")

    categories = ["team", "league", "position", "bats", "throws"]

    for category in categories:
        if guess_player[category] == mystery_player[category]:
            print(f"{category.title()}: Correct")
        else:
            print(f"{category.title()}: {guess_player[category]} is incorrect")

    print()
    