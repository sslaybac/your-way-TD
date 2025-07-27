import pygame
from pygame.math import Vector2
import os

from .constants import CELL_SIZE
from .constants import CELL_PATH
from .constants import DEFAULT_MAP_FILE
from .cell_manager  import find_center
from .cell_manager  import cell_to_rect

# singleton variable.
path = None

class Path():
	"""
	input:
		map_file: txt file containing an encoded map, and the start and end coordinates.

	members:
		grid squares: from input
		coords: pixel coordinates of grid square centers
		distances: list of distances between each pair of coords
		start: first element in coords.
	"""
	def __init__(self, map_file):
		with open(map_file) as f:
			data = f.read().splitlines()
			self.map = data[:-1]
			start = data[-1].split(',')
			self.start = Vector2(int(start[0]), int(start[1]))
			self.build_path()
			self.find_poison_squares()
			self.coords = [Vector2(find_center(p[0], p[1])) for p in self.grid_squares]
			self.distances = self.calculate_distances()
			self.start = self.coords[0]

	"""
	utility function to extract the path from the map given
	in the file.
	"""
	def build_path(self):
		self.grid_squares = [self.start]
		x = int(self.start.x)
		y = int(self.start.y)
		direction = self.map[y][x]
		while direction != 'z':
			match direction:
				case 'n':
					y -= 1
				case 's':
					y += 1
				case 'w':
					x -= 1
				case 'e':
					x += 1
				case 'z':
					pass
				case _:
					raise Exception("Path doesn't reach a valid endpoint")
			self.grid_squares.append(Vector2(x, y))
			direction = self.map[y][x]


	"""
	utility function to find the 'poison' squares that reduce tower effectiveness
	"""
	def find_poison_squares(self):
		self.poison_squares = []
		for y, line in enumerate(self.map):
			x_set = [x for x, ch in enumerate(line) if ch == 'p']
			self.poison_squares += [(x, y) for x in x_set]


	"""
	utility function: calculates distances member
	"""
	def calculate_distances(self):
		distances = []
		for a, b in zip(self.coords, self.coords[1:]):
			dist = a.distance_to(b)
			distances.append(dist)
		return distances

	"""
	input:
		travel distance: how far has the creep traveled along this path.
	return:
		Vector2: 2D pixel location of that distance
	"""
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

	"""
	input:
		travel distance: how far has the creep traveled along this path.
	output: boolean
		True: if travel distance is >= path total length
		False: otherwise
	"""
	def reached_end(self, travel_distance):
		if travel_distance >= sum(self.distances):
			return True
		else:
			return False

	"""
	input: x, y: grid square
	output:
		True: input grid square is directly between 2 grid squares in path
		False: otherwise
		Note: function assumes all paths are horizontal or vertical

	"""
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

	def is_poison(self, grid_x, grid_y):
		if (grid_x, grid_y) in self.poison_squares:
			return True
		else:
			return False
	"""
	1. Draw the path, using the lines(function) thickness is equal to CELL_SIZE
	2. Draw the poison squares, using the rectangle of each cell.
	"""
	def draw(self, screen):
		pygame.draw.lines(screen, "yellow", False, self.coords, CELL_SIZE)
		for point in self.poison_squares:
			rect = cell_to_rect(point[0], point[1])
			pygame.draw.rect(screen, "purple", rect)


# singleton call
def get_path():
	global path
	if path is None:
		path = Path(DEFAULT_MAP_FILE)
	return path