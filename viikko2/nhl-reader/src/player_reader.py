import requests
from player import Player

class PlayerReader:
    def __init__(self, url):
        self.url = url
        self.players = self.get_players()

    def get_players(self):
        players_file = requests.get(self.url).json()

        players = []

        for player_dict in players_file:
            player = Player(player_dict)
            players.append(player)

        return players