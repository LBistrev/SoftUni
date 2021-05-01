team_players_cards = input()
cards = team_players_cards.split()
team_A = 11
team_B = 11
list_A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
list_B = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

for item in cards:
    team, team_number = item.split("-")
    team_number = int(team_number)
    if team_A < 7 or team_B < 7:
        break
    if "A" in item:
        if team_number in list_A:
            list_A.remove(team_number)
            team_A -= 1
    elif "B" in item:
        if team_number in list_B:
            list_B.remove(team_number)
            team_B -= 1

print(f"Team A - {team_A}; Team B - {team_B}")
if team_A < 7 or team_B < 7:
    print("Game was terminated")
