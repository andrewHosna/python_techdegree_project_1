# project 1: build a soccer league
import csv

if __name__ == '__main__':
    experienced_players = list()
    rookie_players = list()

    # iterate over soccer_players.csv, create a list of experienced players and a list of rookie players
    with open("soccer_players.csv", newline='') as csv_file:
        player_reader = csv.DictReader(csv_file, delimiter=',')
        rows = list(player_reader)
        for row in rows:
            if row['Soccer Experience'] == 'YES':
                experienced_players.append({"name": row['Name'], "height": row['Height (inches)'],
                                            "experience": row['Soccer Experience'], "guardian": row['Guardian Name(s)']})
            else:
                rookie_players.append({"name": row['Name'], "height": row['Height (inches)'],
                                            "experience": row['Soccer Experience'], "guardian": row['Guardian Name(s)']})

    print(experienced_players)
    print(rookie_players)

# assign players three teams: dragons, sharks, and raptors
# assignment based on experience, teams must be balanced


# generate output text file 'teams.txt' with a league roster

# generate 18 additional text files for the letters to guardians
# include guardian names, player's name, team name, date & time of first practice
