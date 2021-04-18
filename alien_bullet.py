import pygame
from bullet import Bullet

class AlienBullet(Bullet):
	"""Init ship's bullet"""
	def __init__(self, ai_settings, screen, alien):
		Bullet.__init__(self, ai_settings, screen)

		# Ship bullet position
		self.rect.centerx = alien.rect.centerx
		self.rect.bottom = alien.rect.bottom

		# Store the bullet's position as demical value
		self.y = float(self.rect.y)

	def update(self):
		"""Move the bullet down the screen"""
		# Update the demical position of the alien bullet
		self.y += self.speed_factor
		# Update the rect position
		self.rect.y = self.y
