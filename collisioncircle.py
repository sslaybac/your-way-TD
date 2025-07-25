import pygame

class CollisionCircle(pygame.sprite.Sprite):
	def __init__(x, y, radius)
		if hasattr(self, "containers"):
			super().__init__(self.containers)
		else:
			super().__init__()

	def collided_with(self, other):
		distance = self.position.distance_to(other.position)
		combined_radius = self.radius + other.radius
		if (distance <= combined_radius):
			return True
		else:
			return False
