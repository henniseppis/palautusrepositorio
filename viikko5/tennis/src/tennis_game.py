class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.m_score1 = self.m_score1 + 1
            
        elif player_name == "player2":
            self.m_score2 = self.m_score2 + 1

    def get_score(self):
        self.score = ""
        self.temp_score = 0
        self.game_point = 4

        if self.m_score1 == self.m_score2:
            score = self.same_points()
        
        elif self.m_score1 >= self.game_point or self.m_score2 >= self.game_point:
            score = self.advantage_points()
        
        else:
            score = self.basic_points()
        
        return score
    
    def same_points(self):
            
            # 0 = 0-0, 1 = 15-15, 2 = 30-30, 3 = 40-40 

            if self.m_score1 == 0:
                self.score = "Love-All"
            elif self.m_score1 == 1:
                self.score = "Fifteen-All"
            elif self.m_score1 == 2:
                self.score = "Thirty-All"
            else:
                self.score = "Deuce"
            
            return self.score
    
    def advantage_points(self):
            
            # happens when game is 40-40 == deuce

            advantage = self.m_score1 - self. m_score2

            if advantage == 1:
                self.score = "Advantage player1"
            elif advantage == -1:
                self.score = "Advantage player2"
            elif advantage >= 2:
                self.score = "Win for player1"
            else:
                self.score = "Win for player2"

            return self.score


    def basic_points(self):

        for player_score in [self.m_score1, self.m_score2]:
                if player_score == 0:
                    self.temp_score = self.m_score1
                elif player_score == 1:
                    self.score = self.score + "-"
                    self.temp_score = self.m_score2

                if self.temp_score == 0:
                    self.score = self.score + "Love"
                elif self.temp_score == 1:
                    self.score = self.score + "Fifteen"
                elif self.temp_score == 2:
                    self.score = self.score + "Thirty"
                elif self.temp_score == 3:
                    self.score = self.score + "Forty"
            
        return self.score