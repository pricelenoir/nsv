import sys
import pandas as pd
from nba_functions import valid_player, valid_season

first_name = sys.argv[1].capitalize()
last_name = sys.argv[2].capitalize()
start_season = sys.argv[3]
end_season = sys.argv[4]

player_name = f"{first_name} {last_name}"
    
if not valid_player(player_name):
    print("Invalid player name.")
    sys.exit(1)

if start_season == end_season:
    print("Start season cannot equal end season.")
    sys.exit(1)

# Check that each season is valid
for season in range(int(start_season), int(end_season)):
    season_id = f"{season}-{str(season+1)[2:]}"
    if not valid_season(player_name, season_id):
        print(f"Invalid season: {season_id}.")
        sys.exit(1)