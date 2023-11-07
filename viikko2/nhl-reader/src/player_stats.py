def sort_by_points(player):
    return player.points

class PlayerStats:
    def __init__(self, reader):
        self.reader = reader
        self.players = reader.get_players()

    def top_scorers_by_nationality(self, nationality):

        players = []

        for player in self.players:
            if player.nationality == nationality:
                players.append(player)
        
        sorted_players = sorted(players,reverse=True,key=sort_by_points)
  
        return sorted_players


      
        