import pandas as pd
from nba_api.stats.static import players
from nba_api.stats.endpoints import shotchartdetail, playercareerstats

def valid_player(player_name):
    # Check if player name is valid
    nba_players = players.get_players()
    player_names = [player['full_name'] for player in nba_players]
    
    return player_name in player_names

def valid_season(player_name, season_id):
    # Check if player was playing during particular season(s)
    player_dict = [player for player in players.get_players() if player['full_name'] == player_name]
    if not player_dict:
        return False
    
    player_id = player_dict[0]['id']
    career = playercareerstats.PlayerCareerStats(player_id=player_id)

    career_df = career.get_data_frames()[0]
    return season_id in career_df['SEASON_ID'].values

def get_player_shots(player_name, season_id):
    nba_players = players.get_players()
    player_dict = [player for player in nba_players if player['full_name'] == player_name][0]

    career = playercareerstats.PlayerCareerStats(player_id=player_dict['id'])

    career_df = career.get_data_frames()[0]
    team_id = career_df[career_df['SEASON_ID'] == season_id]['TEAM_ID']

    shotchartlist = shotchartdetail.ShotChartDetail(team_id=team_id, 
                                                   player_id=int(player_dict['id']), 
                                                   season_type_all_star='Regular Season', 
                                                   season_nullable=season_id,
                                                   context_measure_simple="FGA").get_data_frames()
    
    shots_df = shotchartlist[0][['LOC_X', 'LOC_Y', 'SHOT_MADE_FLAG', 'SHOT_TYPE']]
    shots_df.loc[:, 'SHOT_TYPE'] = shots_df['SHOT_TYPE'].map({'2PT Field Goal': 0, '3PT Field Goal': 1})
    return shots_df