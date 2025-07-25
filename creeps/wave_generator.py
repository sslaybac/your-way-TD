from .creep import Creep

class WaveGenerator():
	def __init__(self, num_creeps, production_cooldown):
		self.num_creeps = num_creeps
		self.production_cooldown = production_cooldown
		self.production_timer = production_cooldown

	def update(self, path):
		self.production_timer -= 1
		if (self.production_timer <= 0 and self.num_creeps > 0):
			Creep(path)
			self.num_creeps -= 1
			self.production_timer = self.production_cooldown
