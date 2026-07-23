"""arsenal.py
Joel Bratt
Contains the aresenal and when the bullet is getting removed
Code from the end of following the tutorial
7/23/2026
"""
import pygame
from bullet import Bullet
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Arsenal:
    """Class to manage the collection of bullets fired by ship."""
    def __init__(self, game: 'AlienInvasion'):
        """Initilaizes the arsenal group."""
        self.game = game
        self.settings = game.settings
        self.arsenal = pygame.sprite.Group()

    def update_arsenal(self):
        """Updates the position of bullets and removes old ones."""
        self.arsenal.update()
        self._remove_bullets_offscreen()

    def _remove_bullets_offscreen(self):
        """Removes the bullets that go off the top of screen."""
        for bullet in self.arsenal.copy():
            if bullet.rect.bottom <= 0:
                self.arsenal.remove(bullet)
    
    def draw(self):
        """Draw all bullets to the screen"""
        for bullet in self.arsenal:
            bullet.draw_bullet()
    
    def fire_bullet(self):
        """Fires a new bullet if the limit is not yet reached."""
        if len(self.arsenal) < self.settings.bullet_amount:
            new_bullet = Bullet(self.game)
            self.arsenal.add(new_bullet)
            return True
        return False
