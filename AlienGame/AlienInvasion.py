# -*- coding: utf-8 -*-
"""
Main Module for Alien Game
"""

import sys, os
from time import sleep

import pygame

from settings import Settings
from GameStats import GameStats
from ship import Ship
from bullet import Bullet
from Alien import Alien
from Button import Button
from Scoreboard import Scoreboard

class AlienInvasion:
    """Alien Game"""
    def __init__(self):

        """"Initialize game and settings"""
        pygame.init()
        self.settings = Settings()
        #self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption('Alien Invasion')    
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        self.play_button = Button(self,"Play!!!")

    def run_game(self):
        """begin the game"""
        while True:
            self.CheckEvents() 

            if self.stats.game_active == True:
                self.ship.Update()
                self._update_bullets()
                self._update_aliens()

            self.UpdateScreen()


    def _check_play_button(self, mouse_pos):
        """start a new game if play is clicked"""
        if self.play_button.rect.collidepoint(mouse_pos) and self.stats.game_active == False:
            self.settings.initialize_dynamic_settings()
            self.stats.reset_stats()
            self.stats.game_active = True
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_level()
            self.sb.prep_ships()

            #clear any remaining aliens or bullets and create brand new one
            self.aliens.empty()
            self.bullets.empty()
            self._create_fleet()
            self.ship.center_ship()

            #hide mouse 
            pygame.mouse.set_visible(False)


    def CheckEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)    
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            # move the ship to the right
            self.ship.moving_right = True
        if event.key == pygame.K_LEFT:
            # move the ship to the right
            self.ship.moving_left = True
        if event.key == pygame.K_UP:
            # move the ship to the right
            self.ship.moving_up = True
        if event.key == pygame.K_DOWN:
            # move the ship to the right
            self.ship.moving_down = True
        if event.key == pygame.K_SPACE:
            if len(self.bullets) < self.settings.bullets_allowed:
                self._fire_bullet()
        if event.key == pygame.K_q:                   
            sys.exit()

    def _check_keyup_events(self, event):
        """key release events"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        if event.key == pygame.K_DOWN:
            self.ship.moving_down = False       
            
    def _fire_bullet(self):
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)
    

    def _update_bullets(self):
        self.bullets.update() # draw bullets at new positions
        #delete bullets that are above the screen
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        #check for collissions with alien
        #all objects that have collided are deleted.  for high powered bullet set the first bool to true
        collisions = pygame.sprite.groupcollide(self.bullets,self.aliens,True,True)
        
        if collisions:
            # each dictionary value contains a list of all aliens hit by 1 bullet.
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()

        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()     
            self.settings.increase_speed()

            #increase level
            self.stats.level += 1
            self.sb.prep_level()


    def _update_aliens(self):
        """Check if fleet is on an edge and then if necessary update all alien positions"""
        self._check_fleet_edges()
        self.aliens.update()

        if pygame.sprite.spritecollideany(self.ship,self.aliens):
            self._ship_hit()
        self._check_aliens_bottom()
            
    def _create_fleet(self):
        """create the fleet of aliens"""
        alien = Alien(self)
        alien_width,alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - 2 * alien_width
        number_aliens_x = available_space_x//(2*alien_width)

        #determine number of rows for screen
        ship_height = self.ship.rect.height
        available_space_y = self.settings.screen_height - 3 * alien_height - ship_height
        number_rows = available_space_y // (2 * alien_height)

        #add row of aliens
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)
        
    def _create_alien(self,alien_number,row_number):
        alien = Alien(self)
        alien_width,alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        """respond appropriately if an alien has reached the edge"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """drop whole fleet and change direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *=-1

    def _ship_hit(self):
        """respond to ship being hit by alien"""
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            self.sb.prep_ships()

            #erase all aliens and bullets
            self.aliens.empty()
            self.bullets.empty()

            self._create_fleet()
            self.ship.center_ship()

            # chill out for a second
            sleep(1.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _check_aliens_bottom(self):
        """look and respond if any aliens are at the bottom of the screen"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                #Same functionality as when the ship is hit
                self._ship_hit()

    def UpdateScreen(self):
        self.screen.fill(self.settings.bg_color) #background color to gray
        self.ship.DrawShip() # draw ship
        for bullet in self.bullets.sprites(): # draw bullets
            bullet.draw_bullet()
        self.aliens.draw(self.screen) #draw aliens
        self.sb.show_score()
        if not self.stats.game_active:
            self.play_button.draw_button()
        pygame.display.flip()        

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()

