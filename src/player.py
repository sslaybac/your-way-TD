import sys

from .constants import STARTING_MONEY
from .constants import STARTING_LIFE

from .datastore import get_datastore

# singleton variable
player = None

class Player():
	"""
	constructor
	members:
		money: starts from a constant
		life: starts from a constant
		selected_tower: starts from a constant
	"""
	def __init__(self, starting_money, starting_life):
		self.money = starting_money
		self.life = starting_life
		self.select_tower("default")

	"""
	input: tower name(String)
	assigns selected_tower based on the constant collection
	"""
	def select_tower(self, name):
		self.selected_tower = get_datastore().towers[name]

	"""
	input: cost
	1. check that the player can afford the given tower
	2. return False if the tower is too expensive
	3. oterwise, decrement money member and return True
	"""
	def purchase_tower(self, cost):
		if self.money < cost:
			return False
		else:
			self.money -= cost
			return True

	"""
	input:
		damage: numerical damage from creep reaching end of path
	change state:
		member life reduced by damage
		if life ends <= 0, report game loss and exit program
	"""
	def lose_life(self, damage):
		self.life -= damage
		if self.life <= 0:
			print("YOU LOSE!")
			sys.exit(0)

	"""
	input:
		payment: numerical earning from creep dying
	change state:
		member money increments by payment
	"""
	def earn_bounty(self, payment):
		self.money += payment

#singleton call
def get_player():
	global player
	if player is None:
		player = Player(STARTING_MONEY, STARTING_LIFE)
	return player