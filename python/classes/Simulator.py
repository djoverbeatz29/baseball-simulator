class Simulator:
    def __init__(self, teams, inning=1, bases=[0,0,0], outs=0, score=[0,0]):
        self.teams=teams
        self.inning=1
        self.outs=0
        self.bases=[0,0,0]
        self.score=[0,0]
    
    def simulate(self, its=100):
        game_log = []
        wins = 0
        for i in range(its):
            game = Game([getattr(self, attr) for attr in dir(g) if "__" not in attr])
            result = game.play_game()
            wins += result.winner
            game_log.append(result)
        print(f"The home team won ${wins} out of ${its}, for a winning percentage of {wins / its * 100}%!")
        return game_log