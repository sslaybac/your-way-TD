import pygame

from ..constants import CELL_SIZE
from ..collisioncircle import CollisionCircle

from ..path import get_path
from ..player import get_player

class Creep(CollisionCircle):
	def __init__(self, speed):
		self.travel_distance = 0
		self.move_counter = 1
		self.speed = speed
		super().__init__(get_path().start[0], get_path().start[1], CELL_SIZE/2)

	def update(self):
		self.move()
		if get_path().reached_end(self.travel_distance):
			print("Creep reached end of path.")
			get_player().lose_life(1)
			self.kill()

	def move(self):
		self.move_counter -= 1
		if self.move_counter <= 0:
			self.travel_distance += self.speed
			self.position = get_path().map_position(self.travel_distance)
			self.move_counter = 1

	def draw(self, screen):
		pygame.draw.circle(screen, "red", self.position, self.radius, 0)