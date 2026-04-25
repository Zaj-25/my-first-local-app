import csv

def load_players():
    players_list = []

    with open("players.csv", "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            players_list.append(row)

    return players_list