import pygame, sys, random

from pygame.locals import *

#Made By: Steven Robert 12/2017



#colors of the resources
BLACK = (0,0,0)
BROWN = (153,76,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
GREY = (112,138,144)
RED = (255,0,0)
LIGHTBLUE = (55,55,255)
WHITE = (255,255,255)  

#cloud position
cloudx = -200
cloudy = 0

birbx = -200
birby = 100

puffycloudx = 200
puffycloudy = 200

#constants representing resources
DIRT = 0
GRASS = 1
WATER = 2
COAL = 3
STONE = 4
LAVA = 5
DIAMOND = 6
CLOUD = 7
BIRB = 8
PUFFYCLOUD = 9
WOOD = 10
COBBLE = 11
GLASS = 12
BRICK = 13
SAND = 14
FIRE = 15

#key = {
#		DIRT, 
#		GRASS, 
#		WATER,
#		COAL,
#		STONE,
#		LAVA, 
#		DIAMOND, 
#		CLOUD,
#		PUFFYCLOUD,
#		WOOD, 
#		COBBLE, 
#		GLASS, 
#		BRICK, 
#		SAND,
#		FIRE 
#
#		}

#texture dictionary
textures = {
			DIRT : pygame.image.load('H:/pygame/Minecraft.pngs/dirt.png'),
			GRASS : pygame.image.load('H:/pygame/Minecraft.pngs/grass.png'),
			WATER : pygame.image.load('H:/pygame/Minecraft.pngs/water.png'),
			COAL : pygame.image.load('H:/pygame/Minecraft.pngs/coal.png'),
			STONE : pygame.image.load('H:/pygame/Minecraft.pngs/stone.png'),
			LAVA : pygame.image.load('H:/pygame/Minecraft.pngs/lava.png'),
			DIAMOND : pygame.image.load('H:/pygame/Minecraft.pngs/diamond.png'),
			CLOUD : pygame.image.load('H:/pygame/Minecraft.pngs/cloud.png'),
			BIRB : pygame.image.load('H:/pygame/Minecraft.pngs/birb.png'),
			PUFFYCLOUD : pygame.image.load('H:/pygame/Minecraft.pngs/puffycloud.png'),
			WOOD : pygame.image.load('H:\pygame\Minecraft.pngs/wood.png'),
			COBBLE : pygame.image.load('H:\pygame\Minecraft.pngs/cobble.png'),
			FIRE : pygame.image.load('H:\pygame\Minecraft.pngs/fire.png'),
			GLASS : pygame.image.load('H:\pygame\Minecraft.pngs/glass.png'),
			BRICK : pygame.image.load('H:\pygame\Minecraft.pngs/brick.png'),
			SAND : pygame.image.load('H:\pygame\Minecraft.pngs/sand.png')
			}

#dictionary of the inventory
inventory = {
			DIRT : 0,
			GRASS : 0,
			WATER : 0,
			COAL : 0,
			STONE : 0,
			LAVA : 0,
			DIAMOND : 0,
			WOOD :0,
			COBBLE :0,
			FIRE :0,
			GLASS :0,
			BRICK :0,
			SAND :0
			}
			
#MAPS EACH RESOURCE
controls = {
    DIRT  : 49,     # event 49 is 1 key
    GRASS : 50,     # event 50 is 2 key
    WATER : 51,     # event 51 is 3 key
    COAL  : 52,     
    STONE  : 53,     
    LAVA  : 54,     
    DIAMOND : 55,     
    WOOD  : 56,     
    SAND  : 57    
     }
      

#RULES TO MAKE CRAFTING
craft = {
		WOOD	: { STONE : 1, DIRT : 2},
		FIRE	: { WOOD : 2, STONE : 2},
		COBBLE	: { STONE : 2},
		GLASS	: { FIRE : 1, SAND : 2},
		BRICK	: { STONE : 2, FIRE : 1},
		SAND	: { STONE : 2}
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
resources = [DIRT,GRASS,WATER,COAL,STONE,LAVA,DIAMOND,WOOD,FIRE,SAND,GLASS,COBBLE,BRICK]
#list comprehension for making map
tilemap = [[DIRT for w in range(MAPWIDTH)] for h in range(MAPHEIGHT)]

#sets up the display
pygame.init()
DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILESIZE,MAPHEIGHT*TILESIZE + 50))

#inventory font
INVFONT = pygame.font.Font('FreeSansBold.ttf', 18)

pygame.display.set_caption('M I N E C R F T -- 2 D')
pygame.display.set_icon(pygame.image.load('H:/pygame/Minecraft.pngs/player.png'))

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
			tile = STONE
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

	fpsClock = pygame.time.Clock()
	
	DISPLAYSURF.fill(BLACK)	
		
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
			
			#if (event.key == K_1):
			#	currentTile = tilemap[playerPos[1]][playerPos[0]]
			#	if inventory[DIRT] > 0:
			#		inventory[DIRT] -= 1
			#		tilemap[playerPos[1]][playerPos[0]] = DIRT
			#		inventory[currentTile] += 1
			#		
			#if (event.key == K_2):
			#	currentTile = tilemap[playerPos[1]][playerPos[0]]
			#	if inventory[GRASS] > 0:
			#		inventory[GRASS] -= 1
			#		tilemap[playerPos[1]][playerPos[0]] = GRASS
			#		inventory[currentTile] += 1
			#		
			#if (event.key == K_3):
			#	currentTile = tilemap[playerPos[1]][playerPos[0]]
			#	if inventory[WATER] > 0:
			#		inventory[WATER] -= 1
			#		tilemap[playerPos[1]][playerPos[0]] = WATER
			#		inventory[currentTile] += 1
			#		
			#if (event.key == K_4):
			#	currentTile = tilemap[playerPos[1]][playerPos[0]]
			#	if inventory[COAL] > 0:
			#		inventory[COAL] -= 1
			#		tilemap[playerPos[1]][playerPos[0]] = COAL
			#		inventory[currentTile] += 1
			#		
			#if (event.key == K_5):
			#	currentTile = tilemap[playerPos[1]][playerPos[0]]
			#	if inventory[STONE] > 0:
			#		inventory[STONE] -= 1
			#		tilemap[playerPos[1]][playerPos[0]] = STONE
			#		inventory[currentTile] += 1
			#
			#if (event.key == K_6):
			#	currentTile = tilemap[playerPos[1]][playerPos[0]]
			#	if inventory[LAVA] > 0:
			#		inventory[LAVA] -= 1
			#		tilemap[playerPos[1]][playerPos[0]] = LAVA
			#		inventory[currentTile] += 1
			#		
			#if (event.key == K_7):
			#	currentTile = tilemap[playerPos[1]][playerPos[0]]
			#	if inventory[DIAMOND] > 0:
			#		inventory[DIAMOND] -= 1
			#		tilemap[playerPos[1]][playerPos[0]] = DIAMOND
			#		inventory[currentTile] += 1
        
			#start of the stuff m8
			for key in controls:
				#if this was pressed
				if (event.key == controls[key]):
					#craft if the mouse is pressed
					if pygame.mouse.get_pressed()[0]:
						#if the item can be crafted
						if key in craft:
							#Do we have enough resources?
							canBeMade = True
						#for each item to craft
						for i in craft[key]:
							if craft[key][i] > inventory[i]:
								#if we can't
								canBeMade = False
								break
						#if we can craft it (all resources)
						if canBeMade == True:
							#take each item for crafting
							for i in craft[key]:
								inventory[i] -= craft[key][i]
							#add the crafted item(s)
							inventory[key] += 1
								
						#PLACE if the mouse isn't pressed
						else:
						
							#get the tile player is on
							currentTile = tilemap[playerPos[1]][playerPos[0]]
							#if we have item to place
							if inventory[key] > 0:
								#take from inventory
								inventory[key] -= 1
								#get the tile we are on
								inventory[currentTile] += 1
								#place item
								tilemap[playerPos[1]][playerPos[0]] = key
							
				
		
	#loop through each row
	for row in range(MAPHEIGHT):
		for column in range(MAPWIDTH):
			DISPLAYSURF.blit(textures[tilemap[row][column]], (column*TILESIZE,row*TILESIZE))
	
	DISPLAYSURF.blit(PLAYER,(playerPos[0]*TILESIZE,playerPos[1]*TILESIZE))
	
	#display the cloud
	DISPLAYSURF.blit(textures[CLOUD].convert_alpha(),(cloudx,cloudy))
	#move the cloud left
	cloudx+=2
	#if the cloud has moved past the map
	if cloudx > MAPWIDTH*TILESIZE:
		cloudy= random.randint(0,MAPHEIGHT*TILESIZE)
		cloudx = -200
		
	DISPLAYSURF.blit(textures[BIRB].convert_alpha(),(birbx,birby))
	#move the birb left
	birbx+=6
	#if the birb has moved past the map
	if birbx > MAPWIDTH*TILESIZE:
		birby= random.randint(0,MAPHEIGHT*TILESIZE)
		birbx = -200
		
	DISPLAYSURF.blit(textures[PUFFYCLOUD].convert_alpha(),(puffycloudx,puffycloudy))
	#move the birb left
	puffycloudx-=3
	#if the birb has moved past the map
	if puffycloudx < -200:
		puffycloudy= random.randint(0,MAPHEIGHT*TILESIZE)
		puffycloudx = MAPWIDTH*TILESIZE
		
	
	#display the inventory, starting 10 pixels in
	placePosition = 10
	for item in resources:
		DISPLAYSURF.blit(textures[item],(placePosition,MAPHEIGHT*TILESIZE+20))
		placePosition += 10
		textObj = INVFONT.render(str(inventory[item]), True, WHITE, BLACK)
		DISPLAYSURF.blit(textObj,(placePosition,MAPHEIGHT*TILESIZE+20))
		placePosition += 35
	
	pygame.display.update()
	fpsClock.tick(24)


