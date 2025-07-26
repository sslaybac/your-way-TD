import pygame

from ..constants import PROJECTILE_SPEED
from ..constants import PROJECTILE_RADIUS
from ..collisioncircle import CollisionCircle
from ..cell_manager import left_play_area

class Projectile(CollisionCircle):
	def __init__(self, start, target, damage):
		super().__init__(start, PROJECTILE_RADIUS)
		self.speed = PROJECTILE_SPEED
		self.velocity = (target - start).normalize() * self.speed
		self.color = "white"
		self.damage = damage

	def update(self, creeps):
		self.position += self.velocity
		for creep in creeps:
			if self.collided_with(creep):
				creep.damage(self.damage)
				self.kill()
		if left_play_area(self.position):
			self.kill()

	def draw(self, screen):
		pygame.draw.circle(screen, self.color, self.position, self.radius, 0)
