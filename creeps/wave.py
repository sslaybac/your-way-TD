from .creep import Creep
from ..path import get_path

from ..constants import DEFAULT_CREEP_TEMPLATES 

class Wave():
	"""
	input:
		template: a dictionary, to assign to members
	members:
		num_creeps: how many creeps in this wave
		creep_type: name of the creep template used for the wave
		production_cooldown: time between spawns
		production_timer: ticking timer, based on cooldown
	"""
	def __init__(self, template):
		self.num_creeps = template["num_creeps"]
		self.creep_type = template["creep_type"]
		self.production_cooldown = template["production_cooldown"]
		self.production_timer = self.production_cooldown

	"""
	returns
		True: if no creeps are left to spawn
		False: otherwise
	"""
	def is_empty(self):
		return self.num_creeps <= 0

	"""
	1. Reduce the production timer
	2. If production_timer is ready and there are creeps leftL
		a. spawn a creep
		b. reduce the creep counter
		c. restart the cooldown
	"""
	def update(self):
		self.production_timer -= 1
		if (self.production_timer <= 0 and self.num_creeps > 0):
			Creep(DEFAULT_CREEP_TEMPLATES[self.creep_type])
			self.num_creeps -= 1
			self.production_timer = self.production_cooldown
