import pygame

from ..constants import PATH_WIDTH
from ..collisioncircle import CollisionCircle

class Creep(CollisionCircle):
	def __init__(self, path):
		self.path = path
		self.travel_distance = 0
		super().__init__(path.start[0], path.start[1], PATH_WIDTH/2)

	def draw(self, screen):
		pygame.draw.circle(screen, "red", self.position, self.radius, 2)