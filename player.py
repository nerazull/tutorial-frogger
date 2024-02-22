import pygame

class Player(pygame.sprite.Sprite):
	def __init__(self, pos, groups):
		super().__init__(groups)
		self.image = pygame.Surface((50,50))
		self.image.fill('red')
		self.rect = self.image.get_rect(center = pos)
	
	def input(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_UP]:
			print('Up')
		if keys[pygame.K_DOWN]:
			print('Down')
		if keys[pygame.K_LEFT]:
			print('Left')
		if keys[pygame.K_RIGHT]:
			print('Right')

	def update(self):
		self.input()
