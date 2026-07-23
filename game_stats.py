"""game_stats.py
Joel Bratt
Tracks the scores and saves them to the json contains score formula
Code from the end of following the tutorial
7/23/2026
"""
from pathlib import Path
import json
import math

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class GameStats():

    def __init__(self, game: 'AlienInvasion'):
        self.game = game
        self.settings = game.settings
        self.max_score = 0
        self.init_saved_scores()
        self.reset_stats() 

    def init_saved_scores(self):
        self.path = self.settings.scores_file
        if self.path.exists() and self.path.stat.__sizeof__()> 20:
            contents = self.path.read_text()
            scores = json.loads(contents)
            self.hi_score = scores.get('hi_score', 0)
        else:
            self.hi_score = 0
            self.save_score()

    def save_score(self):
        scores = {
            'hi_score': self.hi_score
        }
        contents = json.dumps(scores, indent=4)
        try:
            self.path.write_text(contents)
        except FileNotFoundError as e:
            print(f'File Not Found: {e}')

    def reset_stats(self):
        self.ships_left = self.settings.ships_left
        self.score = 0
        self.level = 1

    def update(self, collisions):
        #update self.score
        self._update_score(collisions)

        self._update_max_score()
        self._update_hi_score()

    def _update_max_score(self):
        if self.score > self.max_score:
            self.max_score = self.score
            #print(f'Max: {self.max_score}')


    def _update_hi_score(self):
        if self.score > self.hi_score:
            self.hi_score = self.score
            #print(f'hi: {self.hi_score}')

    def _update_score(self, collisions):
        for alien in collisions.values():
            self.score += math.ceil(self.settings.alien_points ** (1 + self.level/4))
            #print(f'Basic: {self.score}')

    def update_level(self):
        self.level += 1