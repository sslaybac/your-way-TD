import pygame
from .button import Button
from .player import get_player


from .cell_manager import get_zone
from .cell_manager import find_center
from .constants import DEFAULT_TOWER_TEMPLATES 

class UI():
	def __init__(self):

		left = 28
		top = 0
		width = 4
		height = 18

		self.rectangle = get_zone(left, top, width, height)
		self.buttons = []
		idx = 0
		for template in DEFAULT_TOWER_TEMPLATES.values():
			if idx % 2 == 0:
				x_val = 29
			else:
				x_val = 31
			self.buttons.append(Button(template, x_val, 3 + 2*(idx//2)))
			idx += 1

	def is_on_ui(self, grid_x, grid_y):
		return (grid_x >= 28)

	def check_selection(self, grid_x, grid_y):
		for button in self.buttons:
			button.check_selection(grid_x, grid_y)


	def draw(self, screen):
		pygame.draw.rect(screen, "brown", self.rectangle)

		lives = get_player().life
		life_text = f"life: {lives}"
		self.draw_text(screen, life_text, 30, 1)

		money = get_player().money
		money_text = f"money: ${money}"
		self.draw_text(screen, money_text, 30, 2)

		for button in self.buttons:
			button.draw(screen)

	def draw_text(self, screen, text, grid_x, grid_y):
		font = pygame.font.Font('freesansbold.ttf', 14)
		text_rendering = font.render(text, "green", "blue")
		text_box = text_rendering.get_rect()
		text_box.center = find_center(grid_x, grid_y)
		screen.blit(text_rendering, text_box)