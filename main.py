import pygame
import sys

from .ui import UI
from .creeps.creep import Creep
from .creeps.wave import Wave
from .towers.tower import Tower
from .towers.projectile import Projectile

from .constants import SCREEN_WIDTH, SCREEN_HEIGHT
from .constants import STARTING_LIFE, STARTING_MONEY
from .constants import CELL_PATH
from .constants import DEFAULT_WAVES_SEQUENCE
from .constants import DEFAULT_TOWER_TEMPLATES 
from .constants import PLAY_AREA_WIDTH 

from .cell_manager import identify_grid_square, find_center
from .cell_manager import get_zone

from .player import get_player
from .path import get_path

def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	running = True

	clock = pygame.time.Clock()
	dt = 0

	# Management groups
	towers = pygame.sprite.Group()
	projectiles = pygame.sprite.Group()
	creeps = pygame.sprite.Group()
	sprites = pygame.sprite.Group()

	Creep.containers = (creeps, sprites)
	Tower.containers = (towers, sprites)
	Projectile.containers = (projectiles, sprites)


	ui = UI()
	waves = []
	for wave in DEFAULT_WAVES_SEQUENCE:
		waves.append(Wave(wave))

	current_wave = waves.pop(0)

	# Main Game Loop
	while running:
		"""
		1. Towers attack 
		2. Projectiles move, then check collisions
		3. Creeps move, then check for victory
		4. Draw background, ui, path, towers, projectiles, creeps
		"""
		# towers.attack(creeps)
		# projectiles.move(creeps)
		current_wave.update()
		if current_wave.is_empty():
			if waves:
				current_wave = waves.pop(0)
			elif len(creeps) == 0:
				print("You Win!")
				sys.exit(0)
		creeps.update()
		towers.update(creeps)
		projectiles.update(creeps)

		screen.fill("black")
		ui.draw(screen)
		get_path().draw(screen)
		for sprite in sprites:
			sprite.draw(screen)

		pygame.display.flip()
		dt = clock.tick(60) / 1000
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
			if event.type == pygame.MOUSEBUTTONUP:
				mousex, mousey = pygame.mouse.get_pos()
				grid_x, grid_y = identify_grid_square(mousex, mousey)
				if ui.is_on_ui(grid_x, grid_y):
					ui.check_selection(grid_x, grid_y)
				elif not get_path().is_on_path(grid_x, grid_y):
					cost = get_player().selected_tower["cost"]
					if get_player().purchase_tower(cost):
						new_tower = Tower(grid_x, grid_y, get_player().selected_tower)

if __name__ == "__main__":
	main()
