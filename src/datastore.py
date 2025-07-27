import json
import glob

from .constants import WAVES_FILE
from .constants import CREEPS_DIR
from .constants import TOWERS_DIR

# Singleton variable
datastore = None

class Datastore():
	def __init__(self):
		self.load_waves()
		self.load_creeps()
		self.load_towers()

	def load_waves(self):
		with open(WAVES_FILE) as waves_file:
			self.waves = json.load(waves_file)

	def load_creeps(self):
		self.creeps = {}
		for jsonfile in glob.glob(CREEPS_DIR + "*json"):
			with open(jsonfile) as creeps_file:
				data = json.load(creeps_file)
				if isinstance(data, dict):
					self.creeps[data["name"]] = data
				elif isinstance(data, list):
					for item in data:
						self.creeps[item["name"]] = item

	def load_towers(self):
		self.towers = {}
		for jsonfile in glob.glob(TOWERS_DIR + "*json"):
			with open(jsonfile) as towers_file:
				data = json.load(towers_file)
				if isinstance(data, dict):
					self.towers[data["name"]] = data
				elif isinstance(data, list):
					for item in data:
						self.towers[item["name"]] = item


def get_datastore():
	global datastore
	if datastore is None:
		datastore = Datastore()
	return datastore
