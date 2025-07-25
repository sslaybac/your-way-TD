import pygame

from .constants import PATH_WIDTH

class Path():
	def __init__(self, coordinates):
		if len(coordinates) < 2:
			raise Exception("Cannot create a path from fewer than 2 coordiantes.")
		self.coordinates = [pygame.math.Vector2(x) for x in coordinates]
		self.distances = self.calculate_distances()
		self.start = coordinates[0]
		self.end = coordinates[-1]

	def calculate_distances(self):
		distances = []
		for a, b in zip(self.coordinates, self.coordinates[1:]):
			dist = a.distance_to(b)
			distances.append(dist)
		return distances

	def map_position(self, travel_distance):
		running_distance = travel_distance
		path_index = 0
		for index, segment in enumerate(self.distances):
			if segment >= running_distance:
				path_index = index
				break
			else:
				running_distance -= segment

		last_coordinate = self.coordinates[path_index]
		next_coordinate = self.coordinates[path_index+1]
		return last_coordinate.move_towards(next_coordinate, running_distance)

	def reached_end(self, travel_distance):
		if travel_distance >= sum(self.distances):
			return True
		else:
			return False

	def draw(self, screen):
		pygame.draw.lines(screen, "yellow", False, self.coordinates, PATH_WIDTH)
