class Team:
    def __init__(self, ranking, name, played, won, draw, lost, gscored, gconceded, gdiff, points):
        self.ranking = ranking
        self.name = name
        self.won = won
        self.played=played
        self.draw = draw
        self.lost = lost
        self.gscored = gscored
        self.gconceded = gconceded
        self.gdiff = gdiff
        self.points = points
        