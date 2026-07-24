"""alien_fleet.py
Joel Bratt
The fleet for the aliens
Code from the end of following the tutorial
7/23/2026
"""
import pygame
from alien import Alien
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
class AlienFleet:
    """A class to manage the fleet of aliens"""
    
    def __init__(self, game:'AlienInvasion'):
        """Initialize the fleet group and attributes."""
        self.game = game
        self.settings = game.settings
        self.fleet = pygame.sprite.Group()
        self.fleet_direction = self.settings.fleet_direction
        self.fleet_drop_speed = self.settings.fleet_drop_speed

        self.create_fleet()

    def create_fleet(self):
        """Create the full fleet of aliens."""
        alien_w = self.settings.alien_w
        alien_h = self.settings.alien_h
        screen_w = self.settings.screen_w
        screen_h = self.settings.screen_h

        fleet_w, fleet_h = self.calculate_fleet_size(alien_w, screen_w, alien_h, screen_h)

        x_offset, y_offset = self.calculate_offset(alien_w, alien_h, screen_w, fleet_w, fleet_h)
        self._create_different_fleet(alien_w, alien_h, fleet_w, fleet_h, x_offset, y_offset)

    def _create_rectangle_fleet(self, alien_w, alien_h, fleet_w, fleet_h, x_offset, y_offset):
        """Populate the fleet in a grid pattern."""
        #not in use currently
        for row in range(fleet_h):
            for col in range(fleet_w):
                current_x = alien_w * col + x_offset
                current_y = alien_h * row + y_offset
                if col % 2 == 0 or row % 2 == 0:
                    continue
                self._create_alien(current_x, current_y)

    def _create_different_fleet(self, alien_w, alien_h, fleet_w, fleet_h, x_offset, y_offset):
        """Populate the fleet in a different shape (wave)."""

        for row in range(fleet_h):
            for col in range(fleet_w):
                if col % 2 == 0 or row % 2 == 0:
                    continue
                
                v_col = col // 2
                
                wave_multiplier = 2 - abs(2 - (v_col % 4))
                
                current_x = alien_w * col + x_offset
                current_y = alien_h * row + y_offset + (wave_multiplier * alien_h)
                
                self._create_alien(current_x, current_y)



    def calculate_offset(self, alien_w, alien_h, screen_w, fleet_w, fleet_h):
        """Calculate the starting offsets for centering the fleet."""
        half_screen = self.settings.screen_h//2
        fleet_horizontal_space = fleet_w * alien_w
        fleet_vertical_space = fleet_h * alien_h
        x_offset = int((screen_w - fleet_horizontal_space)//2)
        y_offset = int((half_screen - fleet_vertical_space)//2)
        return x_offset,y_offset

    def calculate_fleet_size(self, alien_w, screen_w, alien_h, screen_h):
        """Makes the number of aliens that fit in a row and the number of rows."""
        fleet_w = (screen_w//alien_w)
        fleet_h = ((screen_h/2//alien_h))

        if fleet_w % 2 == 0:
            fleet_w -= 1
        else:
            fleet_w -= 2

        if fleet_h % 2 == 0:
            fleet_h -= 1
        else:
            fleet_h -= 2

        return int(fleet_w), int(fleet_h)
    
    def _create_alien(self, current_x:int, current_y:int):
        """Create alien and place in grid"""
        new_alien = Alien(self, current_x, current_y)

        self.fleet.add(new_alien)

    def _check_fleet_edges(self):
        """Responds when when the aliens hit the edge."""
        alien: 'Alien'
        for alien in self.fleet:
            if alien.check_edges():

                self._drop_alien_fleet()
                self.fleet_direction *= -1
                break

    def _drop_alien_fleet(self):
        """Drop the entire fleet down the screen."""
        for alien in self.fleet:
            alien.y += self.fleet_drop_speed


    def update_fleet(self):
        """Checks if the fleet is at an edge, then update the positions of all the aliens in the fleet."""
        self._check_fleet_edges()
        self.fleet.update()


    def draw(self):
        """Draw the fleet to the screen."""
        alien: 'Alien'
        for alien in self.fleet:
            alien.draw_alien()

    def check_collisions(self, other_group):
        """Check the for collisions between the fleet and another sprite group."""
        return pygame.sprite.groupcollide(self.fleet, other_group, True, True)
    
    def check_fleet_bottom(self):
        """Check if any aliens have reached the bottom of the screen."""
        alien: 'Alien'
        for alien in self.fleet:
            if alien.rect.bottom >= self.settings.screen_h:
                return True
        return False
    
    def check_destroyed_status(self):
        """Returns True when the fleet is entirely destroyed."""
        return not self.fleet

        