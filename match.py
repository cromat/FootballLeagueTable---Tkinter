class Match:
    def __init__(self, host, guest, ghost, gguest, teams):
        self.host = host
        self.guest = guest
        self.ghost = int(ghost)
        self.gguest = int(gguest)
        self.teams = teams

    def play(self):
        self.teams[self.host].played += 1
        self.teams[self.host].gscored += self.ghost
        self.teams[self.host].gconceded += self.gguest
        self.teams[self.host].gdiff = self.teams[self.host].gscored - self.teams[self.host].gconceded

        self.teams[self.guest].played += 1
        self.teams[self.guest].gscored += self.gguest
        self.teams[self.guest].gconceded += self.ghost
        self.teams[self.guest].gdiff = self.teams[self.guest].gscored - self.teams[self.guest].gconceded
        
        if self.ghost > self.gguest:
            self.teams[self.host].won += 1
            self.teams[self.guest].lost += 1
            self.teams[self.host].points += 3

        elif self.ghost < self.gguest:
            self.teams[self.guest].won += 1
            self.teams[self.host].lost += 1
            self.teams[self.guest].points += 3

        else:
            self.teams[self.guest].draw += 1
            self.teams[self.host].draw += 1
            self.teams[self.guest].points += 1
            self.teams[self.host].points += 1

        return self.teams


