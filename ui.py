import math
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

from constants import STARTING_LIFE, STARTING_MONEY

class UI():
	def __init__(self, life, money):
		self.life = life
		self.money = money

		self.right = SCREEN_WIDTH
		self.bottom = SCREEN_HEIGHT
		self.top = 0
		self.left = math.floor(0.9 * SCREEN_WIDTH)
		self.height = SCREEN_HEIGHT
		self.width = self.right - self.left


		self.rectangle = pygame.Rect((self.left, self.top), (self.width, self.height))

	def draw(self, screen):
		pygame.draw.rect(screen, "brown", self.rectangle)