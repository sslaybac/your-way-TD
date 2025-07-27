import pygame
import sys

from .ui import UI
from .creeps.creep import Creep
from .creeps.wave import Wave
from .towers.tower import Tower
from .towers.projectile import Projectile

from .constants import SCREEN_WIDTH, SCREEN_HEIGHT
from .constants import STARTING_LIFE, STARTING_MONEY
from .constants import DEFAULT_WAVES_SEQUENCE
from .constants import DEFAULT_TOWER_TEMPLATES 
from .constants import PLAY_AREA_WIDTH 
from .constants import FRAME_RATE

from .cell_manager import identify_grid_square, find_center
from .cell_manager import get_zone

from .player import get_player
from .path import get_path

def main():
	# pygame initialization
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	running = True

	# Clock initialization
	clock = pygame.time.Clock()
	dt = 0

	# Management groups
	towers = pygame.sprite.Group()
	projectiles = pygame.sprite.Group()
	creeps = pygame.sprite.Group()
	sprites = pygame.sprite.Group()

	# assign classes <-> management groups
	Creep.containers = (creeps, sprites)
	Tower.containers = (towers, sprites)
	Projectile.containers = (projectiles, sprites)


	# create: ui, waves
	ui = UI()
	waves = []
	for wave in DEFAULT_WAVES_SEQUENCE:
		waves.append(Wave(wave))

	current_wave = waves.pop(0)

	# Main Game Loop
	while running:
		"""
		1. Update the current wave
		2. Advance to the next wave, if appropriate
		3. If there are no waves left, and no creeps left, declare victory and
			quit.
		4. update (logic) all active creeps
		5. update (logic) all active towers
		6. update (logic) all active projectiles
		"""
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

		"""
		7. draw a black screen
		8. draw UI elements
		9. draw all sprites
		10. Show the user what was drawn
		"""
		screen.fill("black")
		ui.draw(screen)
		get_path().draw(screen)
		for sprite in sprites:
			sprite.draw(screen)
		pygame.display.flip()

		"""
		11. advance the clock(60 FPS)
		12. check for user input
			a. EXIT: close game
			b. mouse click in ui: select tower type
			c. mouse click not in ui: place tower, if there is enough money
		"""
		dt = clock.tick(FRAME_RATE) / 1000
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
