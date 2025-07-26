from .creep import Creep
from ..path import get_path

class Wave():
	def __init__(self, template):
		self.num_creeps = template["num_creeps"]
		self.creep_type = template["creep_type"]
		self.production_cooldown = template["production_cooldown"]
		self.production_timer = self.production_cooldown

	def is_empty(self):
		return self.num_creeps <= 0

	def update(self):
		self.production_timer -= 1
		if (self.production_timer <= 0 and self.num_creeps > 0):
			Creep(5, 10)
			self.num_creeps -= 1
			self.production_timer = self.production_cooldown
