"""settings.py
Joel Bratt
Settings has core game settings like fps and screen dimensions"
Code from the end of following the tutorial
7/23/2026
"""
from pathlib import Path
class Settings:
    def __init__(self):
        self.name: str = '"Man" Invasion - Track 2'
        self.screen_w = 1200
        self.screen_h  = 800
        self.FPS = 60
        self.bg_file = Path.cwd() / 'Assets' / 'images' / 'BackgroundTest2.png'
        self.difficulty_scale = 1.15
        self.scores_file = Path.cwd() / 'Assets' / 'file' / 'scores.json'

        self.ship_file = Path.cwd() / 'Assets' / 'images' / 'ShipReplace.png'
        self.ship_w = 40
        self.ship_h = 60

        self.bullet_file = Path.cwd() / 'Assets' / 'images' / 'BlastReplace.png'
        self.laser_sound = Path.cwd() / 'Assets' / 'sound' / 'laser2.mp3'
        self.impact_sound = Path.cwd() / 'Assets' / 'sound' / 'impactSound2.mp3'
        self.soundtrack = Path.cwd() / 'Assets' / 'sound' / 'soundtrack.mp3'
        self.gameover = Path.cwd() / 'Assets' / 'sound' / 'gameover.mp3'

        self.alien_file = Path.cwd() / 'Assets' / 'images' / 'Alien1.png'
        self.alien_w = 40
        self.alien_h = 40
        self.fleet_direction = 1

        self.button_w = 200
        self.button_h = 50
        self.button = Path.cwd() / 'Assets' / 'images' / 'playbutton.png'

        self.text_color = (255,255,255)
        self.button_font_size = (48)
        self.HUD_font_size = 22
        self.font_file = Path.cwd() / 'Assets' / 'Fonts' / 'Quantico' / 'Quantico-Bold.ttf'

    def initialize_dynamic_settings(self):
        self.ship_speed = 10
        self.ships_left = 3

        self.bullet_w = 25
        self.bullet_h = 60
        self.bullet_speed = 15
        self.bullet_amount = 5

        self.fleet_speed = 2
        self.fleet_drop_speed = 20
        self.alien_points = 50

    def increase_difficulty(self):
        self.ship_speed *= self.difficulty_scale
        self.bullet_speed *= self.difficulty_scale
        self.fleet_speed *= self.difficulty_scale
        self.bullet_amount += 1