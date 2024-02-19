import sys
import pandas as pd
from nba_functions import get_player_shots

if __name__ == "__main__":
    first_name = sys.argv[1].capitalize()
    last_name = sys.argv[2].capitalize()
    start_season = sys.argv[3]
    end_season = sys.argv[4]

    player_name = f"{first_name} {last_name}"

    # Concatenate dataframes from all valid seasons
    all_shots_df = []
    for season in range(int(start_season), int(end_season)):
        season_id = f"{season}-{str(season+1)[2:]}"
        shots_df = get_player_shots(player_name, season_id)
        all_shots_df.append(shots_df)

    shots_df = pd.concat(all_shots_df, ignore_index=True)

    # Print output to stdout
    print(f"{first_name} {last_name} {start_season} {end_season}")
    print(shots_df.to_string(index=False, header=False))