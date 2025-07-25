import pygame
import sys

from .ui import UI
from .path import Path
from .creeps.creep import Creep

from .constants import SCREEN_WIDTH, SCREEN_HEIGHT
from .constants import STARTING_LIFE, STARTING_MONEY
from .constants import SAMPLE_PATH

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


	ui = UI(STARTING_LIFE, STARTING_MONEY)
	path = Path(SAMPLE_PATH)
	creep1 = Creep(path)

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
		creeps.update()

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

if __name__ == "__main__":
	main()
