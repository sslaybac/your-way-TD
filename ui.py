import math
import pygame
from .cell_manager import get_zone
from .constants import SCREEN_WIDTH, SCREEN_HEIGHT

from .constants import STARTING_LIFE, STARTING_MONEY

class UI():
	def __init__(self, life, money):
		self.life = life
		self.money = money

		left = 29
		top = 0
		width = 3
		height = 18

		self.rectangle = get_zone(left, top, width, height)

	def draw(self, screen):
		pygame.draw.rect(screen, "brown", self.rectangle)