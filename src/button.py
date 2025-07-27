import pygame

from .constants import CELL_SIZE
from .collisioncircle import CollisionCircle
from .cell_manager import find_center

from .player import get_player

"""
drawing class for a button
Allows player to select a tower to deploy
"""
class Button(CollisionCircle):
	def __init__(self, template, x, y):
		self.x = x
		self.y = y
		pos = find_center(x, y)
		super().__init__(pos, CELL_SIZE/2)
		self.tower_name = template["name"]
		self.color = template["color"]
		self.is_selected = False

	"""
	input: x,y: grid square of a mouse click
	state change: select a tower to be deployed.
	"""
	def check_selection(self, grid_x, grid_y):
		if self.x == grid_x and self.y == grid_y:
			get_player().select_tower(self.tower_name)

	"""
	Draw this button
	"""
	def draw(self, screen):
		pygame.draw.circle(screen, self.color, self.position, self.radius, 0)
