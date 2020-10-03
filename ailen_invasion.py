import sys  

import pygame
from settings import Settings

def run_game():
	# Initialize game and create screen object
	pygame.init()
	ai_setting = Settings()
	screen = pygame.display.set_mode(
		(ai_setting.screen_width, ai_setting.screen_height))
	pygame.display.set_caption("Alien Invasion")

	#Set background color
	bg_color = (ai_setting.bg_color)

	# Start the main loop for game.
	while True:

		# What for keyboard and mouse events.
		for event in pygame.even.get():
			if event.type == pygame.QUIT:
				sys.exit()

		# Redraw the screen during each pass through the loop. 
		screen.fill(bg_color)

		#Make the most recently drawn screen visible
		pygame.display.flip()

run_game()		 