import pygame, sys

from pygame.locals import *

BLACK = (0,0,0)
BROWN = (153,76,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
GREY = (112,138,144)
RED = (255,0,0)

DIRT = 0
GRASS = 1
WATER = 2
COAL = 3
ROCK = 4
LAVA = 5

textures = {
			DIRT : pygame.image.load('dirt.png'),
			GRASS : pygame.image.load('grass.png'),
			WATER : pygame.image.load('water.png'),
			COAL : pygame.image.load('coal.png'),
			ROCK : pygame.image.load('rock.png'),
			LAVA : pygame.image.load('lava.png')
			}
	
tilemap = [
		[GRASS, COAL, DIRT, ROCK, LAVA],
		[ROCK, WATER, WATER, GRASS, ROCK],
		[COAL, GRASS, WATER, LAVA, LAVA],
		[DIRT, GRASS, LAVA, COAL, ROCK],
		[GRASS, WATER, DIRT, LAVA, ROCK]
		]

TILESIZE = 40
MAPWIDTH = 5
MAPHEIGHT = 5

pygame.init()
DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILESIZE,MAPHEIGHT*TILESIZE))

while True:
	
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	for row in range(MAPHEIGHT):
		for column in range(MAPWIDTH):
			DISPLAYSURF.blit(textures[tilemap[row][column]], (column*TILESIZE,row*TILESIZE))
	pygame.display.update()






