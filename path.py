import pygame

from .constants import CELL_SIZE
from .cell_manager  import find_center

class Path():
	def __init__(self, coordinates):
		if len(coordinates) < 2:
			raise Exception("Cannot create a path from fewer than 2 coordiantes.")
		self.coordinates = [pygame.math.Vector2(find_center(p[0], p[1])) for p in coordinates]
		self.distances = self.calculate_distances()
		self.start = self.coordinates[0]

	def calculate_distances(self):
		distances = []
		for a, b in zip(self.coordinates, self.coordinates[1:]):
			dist = a.distance_to(b)
			distances.append(dist)
		return distances

	def map_position(self, travel_distance):
		remaining_distance = travel_distance
		path_index = 0
		for index, segment in enumerate(self.distances):
			if segment >= remaining_distance:
				path_index = index
				break
			else:
				remaining_distance -= segment

		last_coordinate = self.coordinates[path_index]
		next_coordinate = self.coordinates[path_index+1]
		return last_coordinate.move_towards(next_coordinate, remaining_distance)

	def reached_end(self, travel_distance):
		if travel_distance >= sum(self.distances):
			return True
		else:
			return False

	def draw(self, screen):
		pygame.draw.lines(screen, "yellow", False, self.coordinates, CELL_SIZE)
