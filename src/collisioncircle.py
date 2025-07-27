import pygame

"""
Base class for most sprites in this game
"""
class CollisionCircle(pygame.sprite.Sprite):

	"""
	constructor
	members:
	position: pygame.math.Vector2
	radius: float
	"""
	def __init__(self, position, radius):
		if hasattr(self, "containers"):
			super().__init__(self.containers)
		else:
			super().__init__()

		self.position = position
		self.radius = radius

	"""
	All collision detection is circle-based, as in the boot.dev asteroids
	lessons. The only real changes to this class are a renaming, and the
	change from x,y to a Vector2
	"""
	def collided_with(self, other):
		distance = self.position.distance_to(other.position)
		combined_radius = self.radius + other.radius
		if (distance <= combined_radius):
			return True
		else:
			return False
