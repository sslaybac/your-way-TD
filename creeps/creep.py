import pygame

from ..constants import PATH_WIDTH
from ..collisioncircle import CollisionCircle

class Creep(CollisionCircle):
	def __init__(self, path):
		self.path = path
		self.travel_distance = 0
		self.move_counter = 1
		self.speed = 5
		super().__init__(path.start[0], path.start[1], PATH_WIDTH/2)

	def update(self):
		self.move()
		if self.path.reached_end(self.travel_distance):
			print("Creep reached end of path.")
			self.kill()

	def move(self):
		self.move_counter -= 1
		if self.move_counter <= 0:
			self.travel_distance += self.speed
			self.position = self.path.map_position(self.travel_distance)
			self.move_counter = 1

	def draw(self, screen):
		pygame.draw.circle(screen, "red", self.position, self.radius, 0)