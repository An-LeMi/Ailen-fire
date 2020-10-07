class GameStats():
	"""Track stastics for Alien Invasion."""

	def __init__(self, ai_settings):
		"""Initialize stastics"""
		self.ai_settings = ai_settings
		self.reset_stats()
		self.game_active = False

	def reset_stats(self):
		"""Initialize stastics that can change during the game."""	
		# Reset when restart game
		self.ship_left = self.ai_settings.ship_limit