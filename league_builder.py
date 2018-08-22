# project 1: build a soccer league
import csv

# only run script when explicitly ran
if __name__ == '__main__':
    with open("soccer_players.csv", newline='') as csv_file:
        player_reader = csv.DictReader(csv_file, delimiter=',')
        rows = list(player_reader)
        for row in rows:
            print(row)

# iterate through soccer_players.csv

# assign players three teams: dragons, sharks, and raptors
# assignment based on experience, teams must be balanced

# generate output text file 'teams.txt' with a league roster

# generate 18 additional text files for the letters to guardians
# include guardian names, player's name, team name, date & time of first practice
