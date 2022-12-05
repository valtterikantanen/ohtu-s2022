class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.players = [{"name": player1_name, "score": 0}, {"name": player2_name, "score": 0}]

    def won_point(self, player_name):
        self.players[0]["score"] += 1 if player_name == self.players[0]["name"] else 0
        self.players[1]["score"] += 1 if player_name == self.players[1]["name"] else 0

    def get_score(self):
        verbal_scores = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty", 4: "Deuce"}

        if self.players[0]["score"] == self.players[1]["score"]:
            score = verbal_scores[self.players[0]["score"]]
            score += "-All" if self.players[0]["score"] <= 3 else ""
        elif self.players[0]["score"] >= 4 or self.players[1]["score"] >= 4:
            score_difference = self.players[0]["score"] - self.players[1]["score"]
            score = "Advantage " if abs(score_difference) == 1 else "Win for "
            score += self.players[0]["name"] if score_difference >= 1 else self.players[1]["name"]
        else:
            score = verbal_scores[self.players[0]["score"]] + "-" + verbal_scores[self.players[1]["score"]]

        return score
