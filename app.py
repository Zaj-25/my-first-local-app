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
            print(f"{category.title()}: {guess_player[category]} is Correct")
        else:
            print(f"{category.title()}: {guess_player[category]} is incorrect")

    print()

def play_game():
    mystery_player = random.choice(players_list)
    guesses = 0
    max_guesses = 6

    display_intro()

    while guesses < max_guesses:
        guess = input("Enter your guess: ")
        guess_player = find_player(guess)

        if guess_player is None:
            print("That player is not in the database. Try again.")
            continue
        guesses += 1

        if guess_player["name"].lower() == mystery_player["name"].lower():
            print(f"\nCorrect! The mystery player was {mystery_player['name']}.")
            print(f"You guessed it in {guesses} guesses.")
            return
        
        hints(guess_player, mystery_player)
        print(f"Guesses remaining: {max_guesses - guesses}")

    print("\nGame over!")
    print(f"The mystery player was {mystery_player['name']}.")

play_game()