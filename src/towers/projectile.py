import pygame

from ..constants import PROJECTILE_SPEED
from ..constants import PROJECTILE_RADIUS
from ..collisioncircle import CollisionCircle
from ..cell_manager import left_play_area

"""
Bullets launched from towers.
"""
class Projectile(CollisionCircle):
	"""
	constructor
	input: start (Vector2), target (Vector2), damage (int)
	members: speed(constant), velocity(speed * direction(start->target),
	color(white), damage(parameter))
	"""
	def __init__(self, start, target, damage):
		super().__init__(start, PROJECTILE_RADIUS)
		self.speed = PROJECTILE_SPEED
		self.velocity = (target - start).normalize() * self.speed
		self.color = "white"
		self.damage = damage

	"""
	1. Move the projectile
	2. If we collided with any creeps
		a. damage the creep
		b. kill the projecile
	3. if the projectile leaves the play area
		a. kill the projectile
	"""
	def update(self, creeps):
		self.position += self.velocity
		for creep in creeps:
			if self.collided_with(creep):
				creep.damage(self.damage)
				self.kill()
		if left_play_area(self.position):
			self.kill()

	"""
	Draw the projectile
	"""
	def draw(self, screen):
		pygame.draw.circle(screen, self.color, self.position, self.radius, 0)
