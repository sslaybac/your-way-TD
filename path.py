import pygame

from .constants import CELL_SIZE
from .cell_manager  import find_center

class Path():
	def __init__(self, grid_squares):
		if len(grid_squares) < 2:
			raise Exception("Cannot create a path from fewer than 2 coordiantes.")
		self.grid_squares = grid_squares	
		self.coords = [pygame.math.Vector2(find_center(p[0], p[1])) for p in grid_squares]
		self.distances = self.calculate_distances()
		self.start = self.coords[0]

	def calculate_distances(self):
		distances = []
		for a, b in zip(self.coords, self.coords[1:]):
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

		last_coord = self.coords[path_index]
		next_coord = self.coords[path_index+1]
		return last_coord.move_towards(next_coord, remaining_distance)

	def reached_end(self, travel_distance):
		if travel_distance >= sum(self.distances):
			return True
		else:
			return False

	def is_on_path(self, square_x, square_y):
		for a, b in zip(self.grid_squares, self.grid_squares[1:]):
			a_x = a[0]
			a_y = a[1]
			b_x = b[0]
			b_y = b[1]
			if (a_x == b_x == square_x):
				if (a_y <= square_y <= b_y or b_y <= square_y <= a_y):
					return True
			if (a_y == b_y == square_y):
				if (a_x <= square_x <= b_x or b_x <= square_x <= a_x):
					return True
		return False

	def draw(self, screen):
		pygame.draw.lines(screen, "yellow", False, self.coords, CELL_SIZE)
