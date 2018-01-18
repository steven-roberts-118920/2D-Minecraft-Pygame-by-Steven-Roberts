import pygame, sys, random

from pygame.locals import *

#colors of the resources
BLACK = (0,0,0)
BROWN = (153,76,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
GREY = (112,138,144)
RED = (255,0,0)
LIGHTBLUE = (55,55,255)
WHITE = (255,255,255)

#constants representing resources
DIRT = 0
GRASS = 1
WATER = 2
COAL = 3
ROCK = 4
LAVA = 5
DIAMOND = 6

#texture dictionary
textures = {
			DIRT : pygame.image.load('H:/pygame/Minecraft.pngs/dirt.png'),
			GRASS : pygame.image.load('H:/pygame/Minecraft.pngs/grass.png'),
			WATER : pygame.image.load('H:/pygame/Minecraft.pngs/water.png'),
			COAL : pygame.image.load('H:/pygame/Minecraft.pngs/coal.png'),
			ROCK : pygame.image.load('H:/pygame/Minecraft.pngs/rock.png'),
			LAVA : pygame.image.load('H:/pygame/Minecraft.pngs/lava.png'),
			DIAMOND : pygame.image.load('H:/pygame/Minecraft.pngs/diamond.png')
			}

#dictionary of the inventory
inventory = {
			DIRT : 0,
			GRASS : 0,
			WATER : 0,
			COAL : 0,
			ROCK : 0,
			LAVA : 0,
			DIAMOND : 0
			}
			
#game dimensions	
TILESIZE = 20
MAPWIDTH = 30
MAPHEIGHT = 20

#player image
PLAYER = pygame.image.load('H:/pygame/Minecraft.pngs/player.png')
#player position
playerPos = [0,0]

#the resources
resources = [DIRT, GRASS, WATER, COAL, ROCK, LAVA, DIAMOND]
#list comprehension for making map
tilemap = [[DIRT for w in range(MAPWIDTH)] for h in range(MAPHEIGHT)]

#sets up the display
pygame.init()
DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILESIZE,MAPHEIGHT*TILESIZE + 50))

#inventory font
INVFONT = pygame.font.Font('FreeSansBold.ttf', 18)

#loop thru each row
for rw in range(MAPHEIGHT):
	#loop thru each column in that row
	for cl in range(MAPWIDTH):
		#picks random integer between (x,y)
		randomNumber = random.randint(0,15)
		#Tells each tile what they are and stuff
		if randomNumber == 0 or randomNumber == 1:
			tile = COAL
		elif randomNumber == 2 or randomNumber == 3:
			tile = WATER
		elif randomNumber == 4 or randomNumber == 5 or randomNumber == 6:
			tile = ROCK
		elif randomNumber == 7 or randomNumber == 8 or randomNumber == 9 or randomNumber == 10:
			tile = GRASS
		elif randomNumber == 11 or randomNumber == 12:
			tile = LAVA
		elif randomNumber == 13 or randomNumber == 14:
			tile = DIRT
		elif randomNumber == 15:
			tile = DIAMOND
		#sets the position of each tile to be random
		tilemap[rw][cl] = tile
		
		
while True:
	
	for event in pygame.event.get():
		print(event)
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		
		elif event.type == KEYDOWN:
			if(event.key == K_RIGHT) and playerPos[0] < MAPWIDTH -1:
				playerPos[0] += 1
			if(event.key == K_LEFT) and playerPos[0] > 0:
				playerPos[0] -= 1
			if(event.key == K_UP) and playerPos[1] > 0:
				playerPos[1] -= 1
			if(event.key == K_DOWN) and playerPos[1] < MAPHEIGHT -1:
				playerPos[1] += 1
			if event.key == K_SPACE:
				currentTile = tilemap[playerPos[1]][playerPos[0]]
				inventory[currentTile] += 1
				tilemap[playerPos[1]][playerPos[0]] = DIRT
			
			if (event.key == K_1):
				currentTile = tilemap[playerPos[1]][playerPos[0]]
				if inventory[DIRT] > 0:
					inventory[DIRT] -= 1
					tilemap[playerPos[1]][playerPos[0]] = DIRT
					inventory[currentTile] += 1
					
			if (event.key == K_2):
				currentTile = tilemap[playerPos[1]][playerPos[0]]
				if inventory[GRASS] > 0:
					inventory[GRASS] -= 1
					tilemap[playerPos[1]][playerPos[0]] = GRASS
					inventory[currentTile] += 1
					
			if (event.key == K_3):
				currentTile = tilemap[playerPos[1]][playerPos[0]]
				if inventory[WATER] > 0:
					inventory[WATER] -= 1
					tilemap[playerPos[1]][playerPos[0]] = WATER
					inventory[currentTile] += 1
					
			if (event.key == K_4):
				currentTile = tilemap[playerPos[1]][playerPos[0]]
				if inventory[COAL] > 0:
					inventory[COAL] -= 1
					tilemap[playerPos[1]][playerPos[0]] = COAL
					inventory[currentTile] += 1
					
			if (event.key == K_5):
				currentTile = tilemap[playerPos[1]][playerPos[0]]
				if inventory[ROCK] > 0:
					inventory[ROCK] -= 1
					tilemap[playerPos[1]][playerPos[0]] = ROCK
					inventory[currentTile] += 1
			
			if (event.key == K_6):
				currentTile = tilemap[playerPos[1]][playerPos[0]]
				if inventory[LAVA] > 0:
					inventory[LAVA] -= 1
					tilemap[playerPos[1]][playerPos[0]] = LAVA
					inventory[currentTile] += 1
					
			if (event.key == K_7):
				currentTile = tilemap[playerPos[1]][playerPos[0]]
				if inventory[DIAMOND] > 0:
					inventory[DIAMOND] -= 1
					tilemap[playerPos[1]][playerPos[0]] = DIAMOND
					inventory[currentTile] += 1

	#loop through each row
	for row in range(MAPHEIGHT):
		for column in range(MAPWIDTH):
			DISPLAYSURF.blit(textures[tilemap[row][column]], (column*TILESIZE,row*TILESIZE))
	
	DISPLAYSURF.blit(PLAYER,(playerPos[0]*TILESIZE,playerPos[1]*TILESIZE))
	
	#display the inventory, starting 10 pixels in
	placePosition = 10
	for item in resources:
		DISPLAYSURF.blit(textures[item],(placePosition,MAPHEIGHT*TILESIZE+20))
		placePosition += 30
		textObj = INVFONT.render(str(inventory[item]), True, WHITE, BLACK)
		DISPLAYSURF.blit(textObj,(placePosition,MAPHEIGHT*TILESIZE+20))
		placePosition += 50
	
	pygame.display.update()


