# garaphics management constants
CELL_SIZE = 50
FRAME_RATE = 60
SCREEN_WIDTH = 32 * CELL_SIZE
SCREEN_HEIGHT = 18 * CELL_SIZE
PLAY_AREA_WIDTH = SCREEN_WIDTH - (4 * CELL_SIZE)

#projectile management constants
PROJECTILE_SPEED = 5
PROJECTILE_RADIUS = 5

# player management constants
STARTING_LIFE = 20
STARTING_MONEY = 200

# default collections for path, creeps, waves, and towers
DEFAULT_MAP_FILE = "assets/maps/default_map.txt"
CELL_PATH = [
	(0,1), (27,1), (27,3), (0,3),
	(0,5), (27,5), (27,7), (0,7),
	(0,9), (27,9), (27,11), (0,11),
	(0,13), (27,13), (27,15), (0,15),
	(0,17), (27,17),
]

DEFAULT_CREEP_TEMPLATES = {
	"default": {"name": "default", "speed": 5, "hp": 10, "bounty": 10, "color": "red"},
	"speedy": {"name": "speedy", "speed": 10, "hp": 5, "bounty": 5, "color": "black"},
	"strong": {"name": "strong", "speed": 2, "hp": 20, "bounty": 20, "color": "blue"},
}

DEFAULT_WAVES_SEQUENCE = [
	{"num_creeps": 30, "creep_type": "default", "production_cooldown": 10},
	{"num_creeps": 50, "creep_type": "speedy", "production_cooldown": 5},
	{"num_creeps": 20, "creep_type": "strong", "production_cooldown": 10},
]

DEFAULT_TOWER_TEMPLATES = {
	"default" : {"name": "default", "type": "hitscan", "cost": 100, "damage": 5, "cooldown": 10, "range": 100, "color": "green"},
	"blue_blaster" : {"name": "blue_blaster", "type": "hitscan", "cost": 50, "damage": 2, "cooldown": 10, "range": 100, "color": "blue"},
	"basic_projectile" : {"name": "basic_projectile", "type": "projectile", "cost": 50, "damage": 10, "cooldown": 30, "range": 100, "color": "orange"},
	"basic_AOE" : {"name": "basic_AOE", "type": "AOE", "cost": 200, "damage": 10, "cooldown": 60, "range": 100, "color": "red"},
}
