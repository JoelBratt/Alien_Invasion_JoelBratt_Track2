"""ship.py
Joel Bratt
Ship update, draw and shooting, as well as centering the ship.
Code from the end of following the tutorial
7/23/2026
"""
import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    from arsenal import Arsenal


class Ship: 
    def __init__(self, game: 'AlienInvasion', arsenal: 'Arsenal'):
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.bounds = self.screen.get_rect()

        self.image = pygame.image.load(self.settings.ship_file)
        self.image = pygame.transform.scale(self.image,
                (self.settings.ship_w, self.settings.ship_h)
                )
        
        self.rect = self.image.get_rect()
        self._center_ship()
        self.moving_right = False
        self.moving_left = False
        self.arsenal = arsenal

    def _center_ship(self):
        self.rect.midbottom = self.bounds.midbottom
        self.x = float(self.rect.x)

    def update(self):
        #updating ship position
        self._update_ship_movement()
        self.arsenal.update_arsenal()

    def _update_ship_movement(self):
        temp_speed = self.settings.ship_speed
        if self.moving_right and self.rect.right < self.bounds.right:
            self.x += temp_speed
        if self.moving_left and self.rect.left > self.bounds.left:
            self.x -= temp_speed

        self.rect.x = self.x
        
    def draw(self):
        self.arsenal.draw()
        self.screen.blit(self.image, self.rect)

    def fire(self):
        return self.arsenal.fire_bullet()
    
    def check_collisions(self, other_group):
        if pygame.sprite.spritecollideany(self, other_group):
            self._center_ship()
            return True
        return False