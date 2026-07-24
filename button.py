"""button.py
Joel Bratt
Checks if start button is clicked and draws the start button as well.
Code from the end of following the tutorial
7/23/2026
"""
import pygame.font
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion


class Button:
    """Class to build buttons."""
    def __init__(self, game: 'AlienInvasion', msg):
        """Initialize the button attributes and loads the button image"""
        self.game = game
        self.screen = game.screen
        self.bounds = game.screen.get_rect()
        self.settings = game.settings

        self.image = pygame.image.load(self.settings.button)
        self.image = pygame.transform.scale(
            self.image, 
            (self.settings.button_w, self.settings.button_h)
        )

        self.rect = self.image.get_rect()
        self.rect.center = self.bounds.center

        self.font = pygame.font.Font(self.settings.font_file,
                self.settings.button_font_size)
        self._prep_msg(msg)

        # self.font = pygame.font.Font(self.settings.font_file, 
        #     self.settings.button_font_size)
        # self.rect = pygame.Rect(0,0,self.settings.button_w, self.settings.button_h)
        # self.rect.center = self.bounds.center
        # self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Turn msg into a rendered image and center text on the button."""
        self.msg_image = self.font.render(msg, True, self.settings.text_color, None)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw(self):
        """Draw blank button then draw message."""
        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def check_clicked(self, mouse_pos):
        """Check if the mosuse is on the button."""
        return self.rect.collidepoint(mouse_pos)


