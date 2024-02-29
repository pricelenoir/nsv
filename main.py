import sys
import pandas as pd
from nba_functions import valid_player, valid_season, get_player_shots
from jgraph import jgraph

if __name__ == "__main__":
    first_name = sys.argv[1].capitalize()
    last_name = sys.argv[2].capitalize()
    start_season = sys.argv[3]
    end_season = sys.argv[4] 
    player_name = f"{first_name} {last_name}"

    if not valid_player(player_name):
        print("Invalid player name.")
        sys.exit(1)

    # Check that each season is valid
    for season in range(int(start_season), int(end_season)):
        season_id = f"{season}-{str(season+1)[2:]}"
        if not valid_season(player_name, season_id):
            print(f"Invalid season: {season_id}.")
            sys.exit(1)

    # Concatenate dataframes from all valid seasons
    all_shots_df = []
    for season in range(int(start_season), int(end_season)):
        season_id = f"{season}-{str(season+1)[2:]}"
        shots_df = get_player_shots(player_name, season_id)
        all_shots_df.append(shots_df)

    shots_df = pd.concat(all_shots_df, ignore_index=True)

    jgraph(player_name, start_season, end_season, shots_df)