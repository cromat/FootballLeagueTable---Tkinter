class Team:
    def __init__(self, ranking, name, played=0, won=0, draw=0, lost=0, gscored=0, gconceded=0, gdiff=0, points=0):
        self.ranking = ranking
        self.name = name
        self.won = won
        self.played = played
        self.draw = draw
        self.lost = lost
        self.gscored = gscored
        self.gconceded = gconceded
        self.gdiff = gdiff
        self.points = points

    def __str__(self):
        return "ranking: " + str(self.ranking) + "\nname: " + self.name + "\nwon: " + str(self.won) + "\nplayed: " + \
               str(self.played) + "\ndraw: " + str(self.draw) + "\nlost: " + str(self.lost) + "\ngscored: " + \
               str(self.gscored) + "\ngconceded: " + str(self.gconceded) + "\ngdiff: " + str(self.gdiff) + "\npoints: " \
               + str(self.points) + "\n"

    def __repr__(self):
        return "ranking: " + str(self.ranking) + "\nname: " + self.name + "\nwon: " + str(self.won) + "\nplayed: " + \
               str(self.played) + "\ndraw: " + str(self.draw) + "\nlost: " + str(self.lost) + "\ngscored: " + \
               str(self.gscored) + "\ngconceded: " + str(self.gconceded) + "\ngdiff: " + str(self.gdiff) + "\npoints: " \
               + str(self.points) + "\n"
