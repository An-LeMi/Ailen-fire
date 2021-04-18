import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
	"""A class to manage bullets fired from aliens and ship"""
	def __init__(self, ai_settings, screen):
		"""Creat a bullet object position"""
		super().__init__()    # The bullet inherit from Sprite
		self.screen = screen

		# Creat a bullet rect at (0, 0)
		self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)

		self.color = ai_settings.bullet_color
		self.speed_factor = ai_settings.bullet_speed_factor

	def draw_bullet(self):
		"""Draw bullet to the screen"""
		pygame.draw.rect(self.screen, self.color, self.rect)

