import random

players = ["Mike Trout", "Aaron Judge", "Pete Alonso"]

answer = random.choice(players)

guess = input("Guess the MLB player: ")

if guess == answer:
    print("Correct!")
else:
    print(f"Wrong! The players was {answer}")