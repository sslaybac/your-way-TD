import pygame
from .constants import CELL_SIZE
from .constants import PLAY_AREA_WIDTH
from .constants import SCREEN_HEIGHT

"""
input: x,y coordinates for a grid square
return: x,y pixel coordinates for the center of the grid square
"""
def find_center(x,y):
	left = CELL_SIZE * (x)
	top = CELL_SIZE * (y)
	center_x = left + CELL_SIZE//2
	center_y = top + CELL_SIZE//2
	return pygame.math.Vector2(center_x, center_y)

"""
input: x,y (top left grid coordinates), width, height 
return: a pygame rectangle that covers the area
"""
def get_zone(grid_x, grid_y, width, height):
	x = grid_x * CELL_SIZE
	y = grid_y * CELL_SIZE
	w = width * CELL_SIZE
	h = height * CELL_SIZE
	return pygame.Rect(x, y, w, h)

"""
input: x,y (pixels)
return: x, y (grid square)
"""
def identify_grid_square(x, y):
	grid_x = int(x//CELL_SIZE)
	grid_y = int(y//CELL_SIZE)
	return (grid_x, grid_y)

"""
input: a Vector2 point
return: boolean --
	if the point is outside the playable area: True
	otherwise: False
"""
def left_play_area(point):
	play_area = get_zone(0,0,27,18)
	if play_area.collidepoint(point):
		return False
	else:
		return True

"""
input: grid coordinates of a cell,
return: pygame rectangle for that cell only
"""
def cell_to_rect(grid_x,grid_y):
	x = grid_x * CELL_SIZE
	y = grid_y * CELL_SIZE
	w = CELL_SIZE
	h = CELL_SIZE
	return pygame.Rect(x, y, w, h)

def is_occupied(towers, grid_x, grid_y):
	for tower in towers:
		if tower.is_on_square(grid_x, grid_y):
			return True
	return False