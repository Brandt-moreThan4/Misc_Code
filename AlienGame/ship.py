import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """description of class"""

    def __init__(self, ai_game):
        """Create ship"""
        super().__init__()
        self.screen = ai_game.screen # allows easy access for whole game screen
        self.screen_rect = ai_game.screen.get_rect() # get screen dimensions ( I think)
        self.settings = ai_game.settings

        self.image = pygame.image.load('images/ship.bmp')
        #self.image = pygame.image.load('images/neil.bmp')
        self.rect = self.image.get_rect()

        #ship starts at bottom middle
        self.rect.midbottom = self.screen_rect.midbottom

        #hold shipposition
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        
        
    def DrawShip(self):
        """Draw ship at it's location"""
        self.screen.blit(self.image,self.rect)

    def Update(self):
        """Update ship position"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        self.rect.x = self.x
        self.rect.y = self.y

    def center_ship(self):
        """center ship on the bottom of the screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
