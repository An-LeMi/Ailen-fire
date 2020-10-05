import sys  

import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
# from alien import Alien -  Don't need because don't use ailen in here


def run_game():
	# Initialize game and create screen object
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")

	#Set background color
	bg_color = (ai_settings.bg_color)

	# Make a ship
	ship = Ship(ai_settings,screen)
	
	# Make a bullet
	bullets = Group()

	# Make ailen
	aliens = Group()

	# Creat the fleet of ailens
	gf.creat_fleet(ai_settings, screen, ship, aliens)

	# Start the main loop for game.
	while True:
		gf.check_events(ai_settings, screen, ship, bullets)
		ship.update()
		gf.update_bullets(bullets)
		gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()		 
