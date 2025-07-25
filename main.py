import pygame
import sys

from constants import SCREEN_WIDTH, SCREEN_HEIGHT

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
		# creeps.move()

		screen.fill("black")
		# ui.draw(screen)
		# path.draw(screen)
		# for sprite in sprites:
		#     sprite.draw(screen)

		pygame.display.flip()
		dt = clock.tick(60) / 1000
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return

if __name__ == "__main__":
	main()
