# project 1: build a soccer league
import csv
import random

WELCOME_LETTER = """Dear {},
{} has been placed on the {} for the upcoming season!

We will have the first practice on {}.

Hope to see you all there!
Coach
"""

# randomly and evenly assign a list of players to each team in the league
def assign_to_team(league, player_list):
    players_per_team = len(player_list) // 3
    for team_roster in league.values():
        for random_player in random.sample(player_list, players_per_team):
            team_roster.append(random_player)
            player_list.remove(random_player)


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

    # randomly assign an equal number of experienced and rookie players to each team
    assign_to_team(league, experienced_players)
    assign_to_team(league, rookie_players)

    # export the league roster into 'teams.txt'
    with open("teams.txt", "w") as output_file:
        output_file.write("Soccer League")
        for team_name, team_roster in league.items():
            output_file.write("\n\n{}\n".format(team_name) + "=" * len(team_name))
            for name, height, experience, guardian in team_roster:
                output_file.write("\n{}, {}, {}, {}".format(name, height, experience, guardian))

    # export welcome letters for each player as 'firstname_lastname.txt'
    for team_name, team_roster in league.items():
        first_practice = "August 25th at 10:00 AM"
        for player in team_roster:
            welcome_file = "_".join(player[0].lower().split()) + ".txt"
            with open(welcome_file, "w") as output_file:
                output_file.write(WELCOME_LETTER.format(player[3], player[0], team_name, first_practice))
