class Team:
    def __init__(self, players):
        self.players=players
        self.record = [0, 0]

    def update_record(self, boo):
        if boo:
            self.record[0] += 1
        else:
            self.record[1] += 1 