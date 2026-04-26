import random
from players import load_players

def display_intro():
    print("Welcome to MLB Guessing Game!")
    print("Try to guess the mystery MLB player.")
    print("You will get hints after each incorrect guess.")
    print()

def find_player(guess, players_list):
    for player in players_list:
        if player["name"].lower() == guess.lower():
            return player
    return None

def hints(guess_player, mystery_player):
    print("\nFeedback:")

    categories = ["team", "league", "division", "position", "bats", "throws"]

    for category in categories:
        if guess_player[category] == mystery_player[category]:
            print(f"{category.title()}: {guess_player[category]} is Correct")
        else:
            print(f"{category.title()}: {guess_player[category]} is incorrect")
    #Age Hint
    guess_age = int(guess_player["age"])
    mystery_age = int(mystery_player["age"])

    if guess_age == mystery_age:
        print(f"Age: {guess_age} Correct")
    elif guess_age < mystery_age:
        print(f"Age: {guess_age} (too low)")
    else:
        print(f"Age: {guess_age} (too high)")
    
    #Height Hint
    guess_height = int(guess_player["height"])
    mystery_height = int(mystery_player["height"])

    if guess_height == mystery_height:
        print(f"Height: {guess_height} Correct")
    elif guess_height < mystery_height:
        print(f"Height: {guess_height} (too short)")
    else:
        print(f"Height: {guess_height} (too tall)")

    print()

def show_guess_history(guess_history):
    print("\nGuess History:")

    for number, player in enumerate(guess_history, start=1):
        print(f"{number}. {player['name']} - {player['team']}, {player['league']} {player['division']}, {player['position']}")

def play_game():
    players_list = load_players()
    mystery_player = random.choice(players_list)
    guesses = 0
    max_guesses = 6
    guess_history = []

    display_intro()

    while guesses < max_guesses:
        guess = input("Enter your guess: ")
        guess_player = find_player(guess, players_list)

        if guess_player is None:
            print("That player is not in the database. Try again.")
            continue
        guesses += 1
        guess_history.append(guess_player)

        if guess_player["name"].lower() == mystery_player["name"].lower():
            print(f"\nCorrect! The mystery player was {mystery_player['name']}.")
            print(f"You guessed it in {guesses} guesses.")
            return
        
        hints(guess_player, mystery_player)
        show_guess_history(guess_history)
        print(f"Guesses remaining: {max_guesses - guesses}")

    print("\nGame over!")
    print(f"The mystery player was {mystery_player['name']}.")

def main():
    while True:
        play_game()

        play_again = input("\nDo you want to play again? (y/n): ")

        if play_again.lower() != "y":
            print("Thanks for playing!")
            break

main()