import requests
from pandas import json_normalize

import requests
import pandas as pd


class ExtractMatches:
    def __init__(self, competition_id, season_id):
        self.competition_id = competition_id
        self.season_id = season_id

    def extracting_raw_data(self): 
        read_matches = requests.get(f'https://raw.githubusercontent.com/statsbomb/open-data/master/data/matches/{self.competition_id}/{self.season_id}.json')
        matches = read_matches.json()
        matches_df_raw = pd.json_normalize(matches, sep='_')
        return matches_df_raw
    
    def matches_detail(self):
        self.world_cup_matches = self.extracting_raw_data()

        self.world_cup_matches['ht_manager_name'] = [list(self.world_cup_matches['home_team_managers'][i][0].values())[1] for i in range(64)]
        self.world_cup_matches['aw_manager_name'] = [list(self.world_cup_matches['away_team_managers'][i][0].values())[1] for i in range(64)]

        if self.competition_id == 43 and self.season_id == 106:
            self.world_cup_matches.drop(columns=['home_team_managers', 'away_team_managers', 'metadata_shot_fidelity_version', 'metadata_xy_fidelity_version'], inplace = True)
            return self.world_cup_matches
        else:
            self.world_cup_matches.drop(columns=['home_team_managers', 'away_team_managers'], inplace = True)
            return self.world_cup_matches

matches_2022 = ExtractMatches(43, 106).matches_detail()
matches_2018 = ExtractMatches(43, 3).matches_detail()

all_matches = pd.concat([matches_2018, matches_2022])
