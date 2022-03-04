"""Game settings for the Alien Invasion game."""


class Settings:
    """A class to store all settings for Alien Invasion."""
    def __init__(self):
        """Initialize the games's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed = 3
        self.ship_limit = 100

        # Bullet settings
        self.bullet_speed = 2
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Alien settings
        self.alien_speed = 0.5
        self.fleet_drop_speed = 2
        # A fleet direction of 1 is right, -1 is left.
        self.fleet_direction = 1