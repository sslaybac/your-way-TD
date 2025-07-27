import json

from .constants import WAVES_FILE

# Singleton variable
datastore = None

class Datastore():
	def __init__(self):
		with open(WAVES_FILE) as waves_file:
			self.waves = json.load(waves_file)

def get_datastore():
	global datastore
	if datastore is None:
		datastore = Datastore()
	return datastore
