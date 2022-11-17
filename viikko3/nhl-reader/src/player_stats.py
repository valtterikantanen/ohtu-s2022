class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):
        all_players = self.reader.get_players()
        players = list(filter(lambda player : player.nationality == nationality, all_players))
        players.sort(key=lambda player : player.goals + player.assists, reverse=True)

        return players