import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """bullets fired by the player ship"""

    def __init__(self,ai_game):
        """create bullet from ship's position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # create bullet at rect (0,0) then set it to correct position
        self.rect = pygame.Rect(0,0,self.settings.bullet_width,self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop # mid of bullet should start at middle of ship

        # position value as decimal
        self.y = float(self.rect.y)

    def update(self):
        """move bullet up the screen"""
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        """draw bullet on screen"""
        pygame.draw.rect(self.screen,self.color,self.rect)