class Settings:

	def __init__(self):
		"""Iniitialize the game's setting"""
		# Screen setting.
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230, 230, 230)

		self.ship_speed_factor = 1.5

		# Bullet setting.
		self.bullet_speed_factor = 3
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (60,60,60) #dark gray bullet
		self.bullets_allowed = 1.5