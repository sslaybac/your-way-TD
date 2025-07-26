import pygame
import sys

from .ui import UI
from .path import Path
from .creeps.creep import Creep
from .creeps.wave import Wave
from .towers.tower import Tower

from .constants import SCREEN_WIDTH, SCREEN_HEIGHT
from .constants import STARTING_LIFE, STARTING_MONEY
from .constants import CELL_PATH

from .cell_manager import identify_grid_square, find_center

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


	ui = UI(STARTING_LIFE, STARTING_MONEY)
	path = Path(CELL_PATH)
	wave1 = Wave(30, 5, path)
	tower1 = Tower(20, 2, 100)

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
		wave1.update()
		creeps.update()
		towers.update(creeps)

		screen.fill("black")
		ui.draw(screen)
		path.draw(screen)
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
				new_tower = Tower(grid_x, grid_y, 100)

if __name__ == "__main__":
	main()
