import copy

class Game:
    def __init__(self,
                 teams,
                 inning=1,
                 outs=0,
                 away_or_home=0,
                 bases=[0,0,0],
                 score=[0,0],
                 game_on=True):
        self.teams=teams
        self.inning=inning
        self.outs=outs
        self.away_or_home=away_or_home
        self.bases=bases
        self.score=score
        self.game_on=game_on
        self.current_player=[0,0]

    def walker:
        self.bases.append(0)
        self.bases[0] += 1
        for i in range(3):
            if self.bases[i]==2:
                self.bases[i] -= 1
                self.bases[i+1] += 1
        runs = self.bases[-1]
        self.bases = self.bases[:3]
        self.score[self.away_or_home] += runs

    def hitter(self, hit_type):
        if hit_type == '1B':
            self.bases = [1,0].extend(self.bases)
        elif hit_type == '2B':
            self.bases = [0,1].extend(self.bases)
        elif hit_type == '3B':
            self.bases = [0,0,1].extend(self.bases)
        elif hit_type == 'HR':
            self.bases = [0,0,0,1].extend(self.bases)
        runs = sum(self.bases[3:])
        self.bases = self.bases[:3]
        self.score[self.away_or_home] += runs

    def at_bat(self):
        player=self.teams[self.away_or_home][self.current_player]
        result = player.at_bat()
        if result == 'OUT':
            self.outs += 1
        elif result == 'BB':
            self.walker()
        else:
            self.hitter(result)
        if (self.inning >= 9
            and ((self.outs >= 3 and self.away_or_home == 0)
            or self.away_or_home == 1)
            and self.score[0] < self.score[1])
            or (self.inning >= 9
            and self.outs >= 3
            and self.score[0] > self.score[1]):
            self.game_on = False
        if self.outs >= 3:
            if self.away_or_home == 1:
                self.inning += 1
            self.outs = 0
            self.current_player[self.away_or_home] = (self.current_player[self.away_or_home] + 1) % 9
            self.away_or_home = (self.away_or_home + 1) % 2
            bases = [0, 0, 0]

    def play_game(self):
        while self.game_on:
            self.at_bat()
        final_score = copy.copy(self.score)
        winner = 1 if (self.score[0] < self.score[1]) else 0
        self.inning = 1
        self.outs = 0
        self.away_or_home = 0
        self.bases = [0,0,0]
        self.score = [0,0]
        self.game_on = True
        return {
            "final_score": final_score,
            "winner": winner
        }