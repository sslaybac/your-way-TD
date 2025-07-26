import pygame

from ..collisioncircle import CollisionCircle
from ..constants import CELL_SIZE
from ..cell_manager import find_center

from ..player import get_player

class Tower(pygame.sprite.Sprite):
	def __init__(self, x, y, template):
		if hasattr(self, "containers"):
			super().__init__(self.containers)
		else:
			super().__init__()
		centerpoint = find_center(x, y)
		self.building = CollisionCircle(centerpoint.x, centerpoint.y, CELL_SIZE/2)
		self.range = CollisionCircle(centerpoint.x, centerpoint.y, template["range"])
		self.cooldown = template["cooldown"]
		self.damage = template["damage"]
		self.type = template["type"]
		self.color = template["color"]
		self.timer = 0

	def update(self, creeps):
		if self.timer > 0:
			self.timer -= 1
			return

		targets = self.identify_targets(creeps)
		if not targets:
			return

		self.attack(targets)

	def attack(self, targets):
		if self.type == "hitscan":
			targets[0].damage(self.damage)
			self.timer = self.cooldown

	def identify_targets(self, creeps):
		targets = []
		for creep in creeps:
			if creep.collided_with(self.range):
				targets.append(creep)
		return sorted(targets, key=lambda creep: creep.travel_distance)


	def draw(self, screen):
		pygame.draw.circle(screen, "gray", self.range.position, self.range.radius, 1)
		pygame.draw.circle(screen, self.color, self.building.position, self.building.radius, 0)
