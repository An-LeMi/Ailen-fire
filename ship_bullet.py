import pygame
from bullet import Bullet

class ShipBullet(Bullet):
	"""Init ship's bullet"""
	def __init__(self, ai_settings, screen, ship):
		Bullet.__init__(self, ai_settings, screen)

		# Ship bullet position
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top

		# Store the bullet's position as demical value
		self.y = float(self.rect.y)

	def update(self):
		"""Move the bullet up the screen"""
		# Update the demical position of the bullet
		self.y -= self.speed_factor
		# Update the rect position
		self.rect.y = self.y

