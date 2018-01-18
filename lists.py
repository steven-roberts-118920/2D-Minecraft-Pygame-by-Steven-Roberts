import pygame, sys, random

from pygame.locals import *

BLACK = (0,0,0)
BROWN = (153,76,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
GREY = (112,138,144)
RED = (255,0,0)
LIGHTBLUE = (55,55,255)

DIRT = 0
GRASS = 1
WATER = 2
COAL = 3
ROCK = 4
LAVA = 5
DIAMOND = 6

textures = {
			DIRT : pygame.image.load('dirt.png'),
			GRASS : pygame.image.load('grass.png'),
			WATER : pygame.image.load('water.png'),
			COAL : pygame.image.load('coal.png'),
			ROCK : pygame.image.load('rock.png'),
			LAVA : pygame.image.load('lava.png'),
			DIAMOND : pygame.image.load('diamond.png')
			}

TILESIZE = 20
MAPWIDTH = 30
MAPHEIGHT = 20

resources = [DIRT, GRASS, WATER, COAL, ROCK, DIAMOND]

tilemap = [[DIRT for w in range(MAPWIDTH)] for h in range(MAPHEIGHT)]

pygame.init()
DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILESIZE,MAPHEIGHT*TILESIZE))

for rw in range(MAPHEIGHT):
	for cl in range(MAPWIDTH):
		randomNumber = random.randint(0,15)
		if randomNumber == 0 or randomNumber == 1:
			tile = COAL
		elif randomNumber == 2 or randomNumber == 3:
			tile = WATER
		elif randomNumber == 4 or randomNumber == 5 or randomNumber == 6:
			tile = ROCK
		elif randomNumber == 7 or randomNumber == 8 or randomNumber == 9:
			tile = GRASS
		elif randomNumber == 10 or randomNumber == 11:
			tile = LAVA
		elif randomNumber == 12 or randomNumber == 13 or randomNumber == 14:
			tile = DIRT
		elif randomNumber == 15:
			tile = DIAMOND
		tilemap[rw][cl] = tile
		
while True:
	
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
			
	for row in range(MAPHEIGHT):
		for column in range(MAPWIDTH):
			DISPLAYSURF.blit(textures[tilemap[row][column]], (column*TILESIZE,row*TILESIZE))
	
	pygame.display.update()






