import sys

from .constants import STARTING_MONEY
from .constants import STARTING_LIFE
from .constants import DEFAULT_TOWER_TEMPLATES 

player = None

class Player():
	def __init__(self, starting_money, starting_life):
		self.money = starting_money
		self.life = starting_life
		self.select_tower("default")

	def select_tower(self, name):
		self.selected_tower = DEFAULT_TOWER_TEMPLATES[name]
		print(f"selecting {name}")

	def purchase_tower(self, cost):
		if self.money < cost:
			return False
		else:
			self.money -= cost
			return True

	def lose_life(self, damage):
		self.life -= damage
		if self.life <= 0:
			print("YOU LOSE!")
			sys.exit(0)

	def earn_bounty(self, payment):
		self.money += payment

def get_player():
	global player
	if player is None:
		player = Player(STARTING_MONEY, STARTING_LIFE)
	return player