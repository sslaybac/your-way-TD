import math
import pygame

from ..constants import CELL_SIZE
from ..constants import FRAME_RATE
from ..collisioncircle import CollisionCircle

from ..path import get_path
from ..player import get_player

class Creep(CollisionCircle):
	"""
	input:
		template: dictionary, to assign members
	members:
		travel_distance: how far creep has gone on path, starts at 0
		move_counter: how many frames before next move action
		speed: how many pixels each move counter
		maxHP: starting health (will not change)
		currentHP: health (will decrease to 0)
		bounty: money earned by player on kill
		color: drawing color
	"""
	def __init__(self, template):
		self.travel_distance = 0
		self.move_counter = 1
		self.speed = template["speed"]
		self.normalSpeed = template["speed"]
		self.maxHP = template["hp"]
		self.currentHP = self.maxHP
		self.bounty = template["bounty"]
		self.color = template["color"]
		super().__init__(get_path().start, CELL_SIZE/2)

	"""
	input: damage: amount of damage inflicted
	state change:
		currentHP reduced by damage:
			if <= 0, delete this sprite from its group(s)
	"""
	def damage(self, damage):
		self.currentHP -= damage
		if self.currentHP <= 0:
			get_player().earn_bounty(self.bounty)
			self.kill()

	"""
	state change:
		increase travel_distance based on speed
		if this creep has reached the end of the path:
			ding the player for 1 life
			delete references to this creep
	"""
	def update(self):
		self.move()
		if get_path().reached_end(self.travel_distance):
			print("Creep reached end of path.")
			get_player().lose_life(1)
			self.kill()
		if self.speed < self.normalSpeed:
			self.speed += (self.normalSpeed / FRAME_RATE)

	"""
	state_change:
		increase travel_distance member, based on speed 
		(speed is measured in grid squares / second)
		update pixel position accordingly
		reset cooldown
	"""
	def move(self):
		self.travel_distance += self.speed * CELL_SIZE / FRAME_RATE
		self.position = get_path().map_position(self.travel_distance)
		self.move_counter = 1

	"""
	output:
		pygame rectangle surronding this creep's collision circle
	"""
	def get_rect(self):
		left = self.position.x - self.radius
		top = self.position.y - self.radius
		width = 2 * self.radius
		height = 2 * self.radius
		return pygame.Rect(left, top, width, height)

	"""
	Draws the creep.
	removes circle quadrants based on creep health
	"""
	def draw(self, screen):
		health_percentage = self.currentHP / self.maxHP

		draw_top_right = health_percentage > .75
		draw_top_left = health_percentage > .5
		draw_bottom_left = health_percentage > .25
		draw_bottom_right = health_percentage > 0

		pygame.draw.circle(screen, self.color, self.position, self.radius, 0, draw_top_right, draw_top_left, draw_bottom_left, draw_bottom_right)
