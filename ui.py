import pygame
from .player import get_player

from .cell_manager import get_zone
from .cell_manager import find_center

class UI():
	def __init__(self):

		left = 28
		top = 0
		width = 4
		height = 18

		self.rectangle = get_zone(left, top, width, height)

	def is_on_ui(self, grid_x, grid_y):
		return (grid_x >= 28)

	def draw(self, screen):
		lives = get_player().life
		money = get_player().money

		font = pygame.font.Font('freesansbold.ttf', 14)

		money_text = f"money: ${money}"
		money_screen = font.render(money_text, "green", "blue")
		money_rect = money_screen.get_rect()

		life_text = f"life: {lives}"
		life_screen = font.render(life_text, "green", "blue")
		life_rect = life_screen.get_rect()

		life_rect.center = find_center(30, 1)
		money_rect.center = find_center(30, 2)

		pygame.draw.rect(screen, "brown", self.rectangle)
		screen.blit(life_screen, life_rect)
		screen.blit(money_screen, money_rect)
