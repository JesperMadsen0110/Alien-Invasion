import pygame

class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed = 2.0
        self.ship_limit = 3
        # Bullet settings
        self.bullet_speed = 5.0
        self.bullet_width = 3
        self.bullet_height = 10
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5
        # Alien settings
        self.alien_speed = 3.0
        self.fleet_drop_speed = 20
        # fleet direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # How quickly the game speeds up.
        self.speedup_scale = 1.1
        # How quickly the alien point values increase.
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 3.5
        self.bullet_speed = 7.0
        self.alien_speed = 1.0
        # fleet direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # Scoring settings
        self.alien_points = 50
    
    def increase_speed(self):
        """Increase speed settings and alien poin values."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)
        # Change the fleet direction to the right.
        if self.fleet_direction > 0:
            self.fleet_direction = 1
        else:
            self.fleet_direction = -1
