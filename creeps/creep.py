import math
import pygame

from ..constants import CELL_SIZE
from ..collisioncircle import CollisionCircle

from ..path import get_path
from ..player import get_player

class Creep(CollisionCircle):
	def __init__(self, template):
		self.travel_distance = 0
		self.move_counter = 1
		self.speed = template["speed"]
		self.maxHP = template["hp"]
		self.currentHP = self.maxHP
		self.bounty = template["bounty"]
		super().__init__(get_path().start[0], get_path().start[1], CELL_SIZE/2)

	def damage(self, damage):
		self.currentHP -= damage
		if self.currentHP <= 0:
			get_player().earn_bounty(self.bounty)
			self.kill()

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

	def get_rect(self):
		left = self.position.x - self.radius
		top = self.position.y - self.radius
		width = 2 * self.radius
		height = 2 * self.radius
		return pygame.Rect(left, top, width, height)

	def draw(self, screen):
		health_percentage = self.currentHP / self.maxHP

		draw_top_right = health_percentage > .75
		draw_top_left = health_percentage > .5
		draw_bottom_left = health_percentage > .25
		draw_bottom_right = health_percentage > 0

		pygame.draw.circle(screen, "red", self.position, self.radius, 0, draw_top_right, draw_top_left, draw_bottom_left, draw_bottom_right)
