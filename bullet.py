"""bullet.py
Joel Bratt
Updating and drawing the bullet and takes bullet and screen information from settings
Code from the end of following the tutorial
7/23/2026
"""
import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Bullet(Sprite):
    """A class to manage bullets fired form the ship."""
    def __init__(self, game: 'AlienInvasion'):
        """Create a bullet object at the ships current position"""
        super().__init__()
        self.game = game
        self.screen = game.screen
        self.settings = game.settings

        self.image = pygame.image.load(self.settings.bullet_file)
        self.image = pygame.transform.scale(self.image,
                (self.settings.bullet_w, self.settings.bullet_h)
                )
        
        self.rect = self.image.get_rect()
        self.rect.midtop = game.ship.rect.midtop
        self.y = float(self.rect.y)
    
    def update(self):
        """Moves the bullet up the screen."""
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y
    
    def draw_bullet(self):
        """Draw the bullet to the screen"""
        self.screen.blit(self.image, self.rect)