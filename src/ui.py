import pygame
from .button import Button
from .player import get_player


from .cell_manager import get_zone
from .cell_manager import find_center

from .datastore import get_datastore

class UI():
	"""
	No inputs needed
	members:
	rectangle: the drawing area for the interface panel
	buttons: buttons that allow the player to select a tower
	"""
	def __init__(self):

		left = 28
		top = 0
		width = 4
		height = 18

		self.rectangle = get_zone(left, top, width, height)
		self.buttons = []
		idx = 0
		for template in get_datastore().towers.values():
			if idx % 2 == 0:
				x_val = 29
			else:
				x_val = 31
			self.buttons.append(Button(template, x_val, 3 + 2*(idx//2)))
			idx += 1

	"""
	input: x,y for a grid square
	output: True if the grid square is in the interface panel
		false otherwise
	"""
	def is_on_ui(self, grid_x, grid_y):
		return (grid_x >= 28)


	"""
	Called on a mouse click: which button(if any) was clicked?
	"""
	def check_selection(self, grid_x, grid_y):
		for button in self.buttons:
			button.check_selection(grid_x, grid_y)


	"""
	Draws all images associated with the UI panel
	1. Player lives (text box)
	2. Player money (text box)
	3. Towers (picture buttons)
	"""
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

	"""
	Draws a text box, using provided text and grid coordinates
	"""
	def draw_text(self, screen, text, grid_x, grid_y):
		font = pygame.font.Font('freesansbold.ttf', 14)
		text_rendering = font.render(text, "green", "blue")
		text_box = text_rendering.get_rect()
		text_box.center = find_center(grid_x, grid_y)
		screen.blit(text_rendering, text_box)