"""Game settings for the Alien Invasion game."""


class Settings:
    """A class to store all settings for Alien Invasion."""
    def __init__(self):
        """Initialize the games's static settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (255, 0, 0)
        self.bullets_allowed = 3

        # Alien settings
        self.fleet_drop_speed = 4
        # A fleet direction of 1 is right, -1 is left.
        self.fleet_direction = 1

        # How quickly the game speeds up
        self.speedup_scale = 1.2

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize the settings that change throughout the game."""
        self.ship_speed = 2.5
        self.bullet_speed = 2.75
        self.alien_speed = 0.75

        # Fleet direction of 1 is right, -1 is left.
        self.fleet_direction = 1

    def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
