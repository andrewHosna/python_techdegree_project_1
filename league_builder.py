# project 1: build a soccer league
import csv
import random

if __name__ == '__main__':
    league = {"Dragons": [], "Sharks": [], "Raptors": []}
    experienced_players = list()
    rookie_players = list()

    # iterate over soccer_players.csv, create a list of experienced players and a list of rookie players
    with open("soccer_players.csv", newline='') as csv_file:
        player_reader = csv.DictReader(csv_file, delimiter=',')
        rows = list(player_reader)
        for row in rows:
            if row['Soccer Experience'] == 'YES':
                experienced_players.append((row['Name'], row['Height (inches)'], row['Soccer Experience'],
                                            row['Guardian Name(s)']))
            else:
                rookie_players.append((row['Name'], row['Height (inches)'], row['Soccer Experience'],
                                       row['Guardian Name(s)']))

    experienced_players_per_team = len(experienced_players) // 3
    rookie_players_per_team = len(rookie_players) // 3
    for roster in league.values():
        for random_player in random.sample(experienced_players, experienced_players_per_team):
            roster.append(random_player)
            experienced_players.remove(random_player)
        for random_player in random.sample(rookie_players, rookie_players_per_team):
            roster.append(random_player)
            rookie_players.remove(random_player)

    for team, roster in league.items():
        print("\n{}\n".format(team) + "=" * len(team))
        for name, height, experience, guardian in roster:
            print("{}, {}, {}, {}".format(name, height, experience, guardian))

# generate output text file 'teams.txt' with a league roster

# generate 18 additional text files for the letters to guardians
# include guardian names, player's name, team name, date & time of first practice
