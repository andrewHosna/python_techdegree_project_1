# project 1: build a soccer league
import csv
import random

WELCOME_LETTER = """Dear {},
{} has been placed on the {} for the upcoming season!

We will have the first practice on {}.

Coach
"""

def assign_to_team(league, player_list):
    players_per_team = len(player_list) // 3
    for roster in league.values():
        for random_player in random.sample(player_list, players_per_team):
            roster.append(random_player)
            player_list.remove(random_player)


if __name__ == '__main__':
    league = {"Dragons": [], "Sharks": [], "Raptors": []}
    experienced_players = list()
    rookie_players = list()
    test_list = list()

    # iterate over soccer_players.csv, create a list of experienced players and a list of rookie players
    with open("soccer_players.csv", newline='') as csv_file:
        player_reader = csv.DictReader(csv_file, delimiter=',')
        rows = list(player_reader)
        for row in rows:
            if row['Soccer Experience'] == 'YES':
                experienced_players.append((row['Name'], row['Height (inches)'], row['Soccer Experience'],
                                            row['Guardian Name(s)']))
                test_list.append(row)
            else:
                rookie_players.append((row['Name'], row['Height (inches)'], row['Soccer Experience'],
                                       row['Guardian Name(s)']))

    # randomly assign an equal number of experienced and rookie players to each teams
    assign_to_team(league, experienced_players)
    assign_to_team(league, rookie_players)

    # export the league roster into 'teams.txt'
    with open("teams.txt", "w") as output_file:
        output_file.write("Soccer League")
        for team, roster in league.items():
            output_file.write("\n\n{}\n".format(team) + "=" * len(team))
            for name, height, experience, guardian in roster:
                output_file.write("\n{}, {}, {}, {}".format(name, height, experience, guardian))

    # export welcome letters for each player as 'firstname_lastname.txt'
    for team, roster in league.items():
        for player in roster:
            welcome_file = "_".join(player[0].lower().split()) + ".txt"
            with open(welcome_file, "w") as output_file:
                output_file.write(WELCOME_LETTER.format(player[3], player[0], team, "August 25th at 10:00 AM"))
