import config
import requests
import random

parameters = {
    "key": config.api_key,
    "steamid": "76561198142616412",
    "format": "json",
    "include_appinfo": True,
    "include_played_free_games": True
}

url = "http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001"

response = requests.get(url, params=parameters).json()['response']

games = []

for game in response['games']:
    games.append(game["name"])

print(games[random.randrange(len(games))])
