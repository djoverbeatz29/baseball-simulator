class Player:
    def __init__(self, probs):
        self.probs = pd.Series(probs)
        self.stats = []
        
    def at_bat(self):
        outcome = np.random.choice(self.probs.index, p=self.probs.values)
        self.stats.append(outcome)
        return outcome