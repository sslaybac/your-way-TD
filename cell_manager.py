import pygame
from .constants import CELL_SIZE

def find_center(x,y):
	left = CELL_SIZE * (x)
	top = CELL_SIZE * (y)
	center_x = left + CELL_SIZE//2
	center_y = top + CELL_SIZE//2
	return pygame.math.Vector2(center_x, center_y)

def get_zone(grid_x, grid_y, width, height):
	x = grid_x * CELL_SIZE
	y = grid_y * CELL_SIZE
	w = width * CELL_SIZE
	h = height * CELL_SIZE
	return pygame.Rect(x, y, w, h)

def identify_grid_square(x, y):
	grid_x = int(x//CELL_SIZE)
	grid_y = int(y//CELL_SIZE)
	return (grid_x, grid_y)
