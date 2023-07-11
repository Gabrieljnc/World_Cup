import requests
from pandas import json_normalize
from matches import ExtractMatches
import pandas as pd


class ExtractEvents:
    def __init__(self):
        self.all_matches_ids = self.matches_ids()

    def matches_ids(self):
        extract_worldcup_2018_matches_df = ExtractMatches(43, 3).matches_detail()['match_id']
        extract_worldcup_2022_matches_df = ExtractMatches(43, 106).matches_detail()['match_id']
        all_matches_ids = sorted(pd.concat([extract_worldcup_2018_matches_df, extract_worldcup_2022_matches_df]))
        return all_matches_ids
    
    def normalize_data(self, match_id):
        read_events = requests.get(f"https://raw.githubusercontent.com/statsbomb/open-data/master/data/events/{match_id}.json")       
        events = read_events.json() 
        events_df = json_normalize(events, sep = '_')
        return events_df

    def get_event(self, match_id):
        if match_id in self.all_matches_ids:
            match_events_raw = self.normalize_data(match_id)
            match_eventes_df = match_events_raw.drop(columns={'tactics_lineup'}) #'shot_freeze_frame'
            match_eventes_df['match_id'] = match_id
            match_eventes_df['year'] = 2018 if match_id < 9000 else 2022
            return match_eventes_df
        else:
            print(f"Match {match_id} not found")
            return None
    
extractor = ExtractEvents()
matches_ids = ExtractEvents().matches_ids()

frames = {event_id: extractor.get_event(event_id) for event_id in matches_ids}

all_data_events = pd.concat(frames.values(), ignore_index=True)
all_data_events.to_csv('dados_eventos_shot_freeze.csv', index=False)



