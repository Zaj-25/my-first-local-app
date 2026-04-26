from colorama import Fore, Style, init
init()
import random
from players import load_players

#Symbols
CHECK = "✅"
CROSS = "❌"
UP = "⬆️"
DOWN = "⬇️"
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
        print(Fore.GREEN + f"Age: {guess_age} Correct" + Style.RESET_ALL)
    elif guess_age < mystery_age:
        print(Fore.YELLOW + f"Age: {guess_age} (too low)" + Style.RESET_ALL)
    else:
        print(Fore.YELLOW + f"Age: {guess_age} (too high)" + Style.RESET_ALL)
    
    #Height Hint
    guess_height = int(guess_player["height"])
    mystery_height = int(mystery_player["height"])

    if guess_height == mystery_height:
        print(Fore.GREEN + f"Height: {guess_height} Correct" + Style.RESET_ALL)
    elif guess_height < mystery_height:
        print(Fore.YELLOW + f"Height: {guess_height} (too short)" + Style.RESET_ALL)
    else:
        print(Fore.YELLOW + f"Height: {guess_height} (too tall)" + Style.RESET_ALL)

    print()

def get_results_symbols(guess_player, mystery_player):
    categories = ["team", "league", "division", "position", "bats", "throws",]
    symbols = []

    for cateogry in categories:
        if guess_player[cateogry] == mystery_player[cateogry]:
            symbols.append(Fore.GREEN + CHECK + Style.RESET_ALL)
        else:
            symbols.append(Fore.RED + CROSS + Style.RESET_ALL)
    
    guess_age = int(guess_player["age"])
    mystery_age = int(mystery_player["age"])

    if guess_age == mystery_age:
        symbols.append(Fore.GREEN + CHECK + Style.RESET_ALL)
    elif guess_age < mystery_age:
        symbols.append(Fore.YELLOW + UP + Style.RESET_ALL)
    else:
        symbols.append(Fore.YELLOW + DOWN + Style.RESET_ALL)
    
    guess_height = int(guess_player["height"])
    mystery_height = int(mystery_player["height"])

    if guess_height == mystery_height:
        symbols.append(Fore.GREEN + CHECK + Style.RESET_ALL)
    elif guess_height < mystery_height:
        symbols.append(Fore.YELLOW + UP + Style.RESET_ALL)
    else:
        symbols.append(Fore.YELLOW + DOWN + Style.RESET_ALL)
    
    return symbols

def show_guess_history(guess_history, mystery_player):
    print("\nGuess History:")
    print("Name | Team | League | Division | Position | Bats | Throws | Age | Height")
    print("-" * 85)

    for number, player in enumerate(guess_history, start=1):
        symbols = get_results_symbols(player, mystery_player)
        symbols_text = " | ".join(symbols)

        print(f"{number}. {player['name']} | {symbols_text}")

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