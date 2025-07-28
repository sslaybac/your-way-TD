import pygame

from ..collisioncircle import CollisionCircle
from ..constants import CELL_SIZE
from ..cell_manager import find_center

from ..player import get_player
from .projectile import Projectile
from ..path import get_path

class Tower(pygame.sprite.Sprite):
	def __init__(self, x, y, template):
		if hasattr(self, "containers"):
			super().__init__(self.containers)
		else:
			super().__init__()
		self.x = x
		self.y = y
		centerpoint = find_center(x, y)
		self.building = CollisionCircle(centerpoint, CELL_SIZE/2)
		self.range = CollisionCircle(centerpoint, template["range"])
		self.cooldown = template["cooldown"]
		self.damage = template["damage"]
		self.type = template["type"]
		self.color = template["color"]
		self.timer = 0
		self.exp = 0
		self.level = 1
		if get_path().is_poison(x, y):
			self.cooldown *= 2

	"""
	1. If appropriate, step through the cooldown
	2. Get a list of all creeps in range
	3. If cooldown is 0 and there is a target, attack.
	"""
	def update(self, creeps):
		if self.timer > 0:
			self.timer -= 1
			return

		targets = self.identify_targets(creeps)
		if not targets:
			return

		self.attack(targets)

		self.exp += 1
		if self.exp == 100:
			self.level += 1
			self.exp = 0

	"""
	Determine what type of tower we are, then attack the target(s)
	types:
	1. "hitscan": 1 target takes instant damage
	2. "projectile": fire off a bullet at the chosen target
	"""
	def attack(self, targets):
		self.timer = self.cooldown
		if self.type == "hitscan":
			targets[0].damage(self.damage * self.level)
			self.timer = self.cooldown
		elif self.type == "projectile":
			self.launch_projectile_at(targets[0])
		elif self.type == "AOE":
			for target in targets:
				target.damage(self.damage * self.level)
		elif self.type == "slow":
			for target in targets:
				target.damage(self.damage * self.level)
				target.speed = 0
		else:
			print("No attack Action for {self.type}")

	def launch_projectile_at(self, target):
		Projectile(self.building.position.copy(), target.position.copy(), self.damage * self.level)

	"""
	Go through the creeps Group and return a list of all members that are in 
	range of this tower. The list will be sorted so that the frontmost creep
	is in position 0
	"""
	def identify_targets(self, creeps):
		targets = []
		for creep in creeps:
			if creep.collided_with(self.range):
				targets.append(creep)
		return_list = sorted(targets, reverse=True, key=lambda creep: creep.travel_distance)
		return return_list

	"""
	Used to prevent stacking towers on a square.
	"""
	def is_on_square(self, target_x, target_y):
		if self.x == target_x and self.y == target_y:
			return True
		else:
			return False


	"""
	1. Draw the tower building
	2. Draw the range ring
	3. If the tower fired in the last 5 frames, draw a light so
		the player knows that the tower fired.
	"""
	def draw(self, screen):
		pygame.draw.circle(screen, "gray", self.range.position, self.range.radius, 1)
		pygame.draw.circle(screen, self.color, self.building.position, self.building.radius, 0)
		for l in range(self.level):
			pygame.draw.circle(screen, "black", self.building.position, l*5, 1)
		if self.timer > self.cooldown -5:
			pygame.draw.circle(screen, "red", self.range.position, 5, 0)
