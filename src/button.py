import pygame

import math

from .constants import CELL_SIZE
from .collisioncircle import CollisionCircle
from .cell_manager import find_center
from .cell_manager import cell_to_rect

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
		if self.tower_name == "default":
			self.is_selected = True
		else:
			self.is_selected = False

	"""
	input: x,y: grid square of a mouse click
	state change: select a tower to be deployed.
	"""
	def check_selection(self, grid_x, grid_y):
		if self.x == grid_x and self.y == grid_y:
			get_player().select_tower(self.tower_name)
			self.is_selected = True
		else:
			self.is_selected = False

	"""
	Draw this button
	"""
	def draw(self, screen):
		pygame.draw.circle(screen, self.color, self.position, self.radius, 0)
		if self.is_selected == True:
			pygame.draw.arc(screen, "yellow", cell_to_rect(self.x, self.y), 0, 2*math.pi, 5)
