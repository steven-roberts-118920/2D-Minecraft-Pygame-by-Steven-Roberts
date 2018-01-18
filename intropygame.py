import pygame, sys

from pygame.locals import *

pygame.init()

DISPLAYSURF = pygame.display.set_mode((300,300))

pygame.display.set_caption('My First Game')

while True:
	
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	pygame.draw.rect(DISPLAYSURF, (255,0,255), (250,250,100,10))
	pygame.draw.rect(DISPLAYSURF, (0,255,0), (100,50,20,20))
	pygame.draw.rect(DISPLAYSURF, (0,0,255), (50,100,50,50))
	pygame.draw.rect(DISPLAYSURF, (255,0,0), (200,50,100,100))
	pygame.draw.circle(DISPLAYSURF, (0,0,255), (150,100),25,25)
	pygame.draw.circle(DISPLAYSURF, (255,255,255), (350,350),1)
	pygame.draw.line(DISPLAYSURF, (255,255,255),(60, 120), (120, 120), 1)
	pygame.draw.line(DISPLAYSURF,(0,255,0),(200,100),(200,356),1)
	pygame.draw.arc(DISPLAYSURF, (0,150,0),(200,10,150,100), 0, 20)
	pygame.display.update()
	
	





