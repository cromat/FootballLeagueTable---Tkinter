#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

class Team:
    def __init__(self, name, played=0, won=0, draw=0, lost=0, gscored=0, gconceded=0, gdiff=0, points=0):
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
        return "name: " + self.name.encode('cp1250', 'ignore').decode('cp1250', 'ignore') + "\nwon: " + str(self.won) + "\nplayed: " + \
               str(self.played) + "\ndraw: " + str(self.draw) + "\nlost: " + str(self.lost) + "\ngscored: " + \
               str(self.gscored) + "\ngconceded: " + str(self.gconceded) + "\ngdiff: " + str(self.gdiff) + "\npoints: " \
               + str(self.points) + "\n"

    def __repr__(self):
        return "name: " + self.name.encode('cp1250', 'ignore').decode('cp1250', 'ignore') + "\nwon: " + str(self.won) + "\nplayed: " + \
               str(self.played) + "\ndraw: " + str(self.draw) + "\nlost: " + str(self.lost) + "\ngscored: " + \
               str(self.gscored) + "\ngconceded: " + str(self.gconceded) + "\ngdiff: " + str(self.gdiff) + "\npoints: " \
               + str(self.points) + "\n"

    def to_JSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, ensure_ascii=False).encode('cp1250', 'ignore').decode('cp1250', 'ignore')
