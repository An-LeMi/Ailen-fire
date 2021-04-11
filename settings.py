class Settings:

	def __init__(self):
		"""Iniitialize the game's setting"""
		# Screen setting.
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230, 230, 230)	

		# Show fps flag
        # self.fps = 60
        # self.show_fps = True

		#Ship setting
		self.ship_speed_factor = 10		
		self.ship_limit = 3			# number ship

		# Bullet setting.
		self.bullet_speed_factor = 3
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (60,60,60) #dark gray bullet
		self.bullets_allowed = 6		# number bullet in screen

		#Alien setting.
		self.alien_speed_factor = 3
		self.fleet_drop_speed = 50
		# fleet_direction of 1 represents right; -1 represents left. 
		self.fleet_direction = 1

		# Scoring
		self.alien_points = 50

		# How quickly the game speed ups
		self.speedup_scale = 1.1
		self.iniitialize_dynamic_settings()
		# How quickly score increase.
		self.score_scale = 1.5

	def iniitialize_dynamic_settings(self):
		"""Iniitialize settings that change throughout the game."""
		self.speed_factor = 1.5
		self.bullet_speed_factor = 3
		self.alien_speed_factor = 1

		# fleet_direction of 1 represents right; -1 represents left. 
		self.fleet_direction = 1	

	def increase_speed(self):
		"""Increase speed settings"""
		self.ship_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale	
		self.alien_points = int(self.alien_points * self.score_scale)