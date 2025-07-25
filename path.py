import pygame

from .constants import PATH_WIDTH

class Path():
	def __init__(self, coordinates):
		if len(coordinates) < 2:
			raise Exception("Cannot create a path from fewer than 2 coordiantes.")
		self.coordinates = coordinates
		self.start = coordinates[0]
		self.end = coordinates[-1]

	def draw(self, screen):
		pygame.draw.lines(screen, "yellow", False, self.coordinates, PATH_WIDTH)
