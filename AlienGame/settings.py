
class Settings:
    """Control the games settings"""

    #set initial values
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)

        #ship settings
        self.ship_limit = 3

        #Bullet settings. Should be in its own class?
        self.bullet_width = 4 #4
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 30

        #alien settings
        self.fleet_drop_speed = 10

        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """these settings change throughout the game"""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        self.alien_points = 50

        #1 means fleet moves right. -1 means fleet moves left
        self.fleet_direction = 1

        
    def increase_speed(self):
        """increase speed and points """
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)