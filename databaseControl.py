import pandas
from Player import Player

def create_DB():
    db = pandas.read_csv("common_player_info.csv")
    return db


def search_player(playerFirstName: str, playerLastName: str, db):
    player_data = db.loc[
        (db['first_name'].str.upper() == playerFirstName.upper()) &
        (db['last_name'].str.upper() == playerLastName.upper()),
        ['first_name', 'last_name', 'rosterstatus', 'season_exp', 'team_name']
    ]
    if not player_data.empty:
        row = player_data.iloc[0]
        player = Player(row['first_name'], row['last_name'], row['rosterstatus'], row['season_exp'], row['team_name'])
        return player
    return None