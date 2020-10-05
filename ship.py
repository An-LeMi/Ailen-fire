import pygame

class Ship():

	def __init__(self, ai_settings, screen):
		"""dInitialize the ship and set its starting position."""
		self.screen = screen
		self.ai_settings = ai_settings

		# Load the ship image and get its rect.
		self.image = pygame.image.load('image/ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		self.rect.centerx = self.screen_rect.centerx  # dat o truc x
		self.rect.bottom = self.screen_rect.bottom    # dat giua 

		self.center = float(self.rect.centerx)   #return value of rect.centerx

		# Movement flag
		self.moving_right = False 
		self.moving_left = False


	def update(self):
		"""Update the ship's position based on the movement flag"""
		# Update the ship's center value, not a rect value
		if self.moving_right and self.rect.centerx < self.screen_rect.right:
			self.center += self.ai_settings.ship_speed_factor	

		if self.moving_left and self.rect.centerx > 0:
			self.center -= self.ai_settings.ship_speed_factor

		# Update rect value base on center
		self.rect.centerx = self.center	

	def blitme(self):
		"""Draw the ship at its current location."""
		self.screen.blit(self.image, self.rect)
