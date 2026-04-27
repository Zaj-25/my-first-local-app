from colorama import Fore, Style, init
init()
import random
from players import load_players

#Symbols
GREEN = "🟩"
RED = "🟥"
YELLOW = "🟨"

def display_intro():
    print("Welcome to MLB Guessing Game!")
    print("Try to guess the mystery MLB player.")
    print("You will get hints after each incorrect guess.")
    print()

def find_player(guess, players_list):
    guess = guess.lower().strip()

    matches = []

    for player in players_list:
        player_name = player["name"].lower()

        if guess == player_name:
            return player
        
        if guess in player_name:
            matches.append(player)
    
    if len(matches) == 1:
        return matches[0]
    
    if len(matches) > 1:
        print("\nMultiple players matched your guess:")
        for player in matches:
            print(f"- {player['name']}")
        print("Please type a more specific name.")
        return None
    
    return None

def hints(guess_player, mystery_player):
    print("\nFeedback:")

    categories = ["team", "league", "division", "position", "bats", "throws"]

    for category in categories:
        if guess_player[category] == mystery_player[category]:
            print(Fore.GREEN + f"{category.title()}: {guess_player[category]} is Correct" + Style.RESET_ALL)
        else:
            print(Fore.RED + f"{category.title()}: {guess_player[category]} is incorrect" + Style.RESET_ALL)
    #Age Hint
    guess_age = int(guess_player["age"])
    mystery_age = int(mystery_player["age"])

    if guess_age == mystery_age:
        print(Fore.GREEN + f"Age: {guess_age} is Correct" + Style.RESET_ALL)
    elif abs(guess_age - mystery_age) <= 2:
        print(Fore.YELLOW + f"Age: {guess_age} is Close" + Style.RESET_ALL)
    else:
        print(Fore.RED + f"Age: {guess_age} is Incorrect" + Style.RESET_ALL)
    
    #Height Hint
    guess_height = int(guess_player["height"])
    mystery_height = int(mystery_player["height"])

    if guess_height == mystery_height:
        print(Fore.GREEN + f"Height: {guess_height} is Correct" + Style.RESET_ALL)
    elif abs(guess_height - mystery_height) <= 2:
        print(Fore.YELLOW + f"Height: {guess_height} is Close" + Style.RESET_ALL)
    else:
        print(Fore.RED + f"Height: {guess_height} is incorrect" + Style.RESET_ALL)

    print()

def get_results_symbols(guess_player, mystery_player):
    categories = ["team", "league", "division", "position", "bats", "throws"]
    results = []

    for cateogry in categories:
        if guess_player[cateogry] == mystery_player[cateogry]:
            results.append(GREEN)
        else:
            results.append(RED)
    
    guess_age = int(guess_player["age"])
    mystery_age = int(mystery_player["age"])

    if guess_age == mystery_age:
        results.append(GREEN)
    elif abs(guess_age - mystery_age) <= 2:
        results.append(YELLOW)
    else:
        results.append(RED)
    
    guess_height = int(guess_player["height"])
    mystery_height = int(mystery_player["height"])

    if guess_height == mystery_height:
        results.append(GREEN)
    elif abs(guess_height - mystery_height) <= 2:
        results.append(YELLOW)
    else:
        results.append(RED)
    
    return results

def show_guess_history(guess_history, mystery_player):
    print("\nGuess History:\n")

    for number, player in enumerate(guess_history, start=1):
        results = get_results_symbols(player, mystery_player)
        squares = " ".join(results)
        print(f"{number}. {player['name']:<20} {squares}")
    
    print()

def choose_difficulty():
    while True:
        print("\nChoose a difficulty:")
        print("1. Easy - 8 guesses")
        print("2. Medium - 6 guesses")
        print("3. Hard - 4 guesses")

        choice = input("Enter 1, 2, or 3: ").strip()

        if choice == "1":
            return 8
        elif choice == "2":
            return 6
        elif choice == "3":
            return 4
        else:
            print("Invalid option. Please try again.\n")

def play_game():
    players_list = load_players()
    mystery_player = random.choice(players_list)
    guesses = 0
    guess_history = []

    display_intro()
    max_guesses = choose_difficulty()

    print(f"\nYou have {max_guesses} guesses. Good luck!")
    print(f"Legend: {GREEN} Corect | {RED} Incorrect | {YELLOW} Close\n")

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
            show_guess_history(guess_history, mystery_player)
            return
        
        hints(guess_player, mystery_player)
        show_guess_history(guess_history, mystery_player)
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