class GameStats:
    """Track game stats for Alien Invasion."""
    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings

        # Start game in an inactive state.
        self.game_active = True
        self.reset_stats()

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit