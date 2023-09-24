import numpy as np
import random as rdm
import pygame
import player
import map
 
#-------------------------------------------------------------------------------------#
#
#-------------------------------------------------------------------------------------#

MAP_W = 36
MAP_H = 28
player = player.Player("Julius")

WIDTH = 1920
HEIGHT = 1080
map = map.Map(MAP_W, MAP_H, WIDTH, HEIGHT)
 
pygame.init()
gameDisplay = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Game')
clock = pygame.time.Clock()

############################################ 

def generate_frame(map):
	img = np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8)
	map.draw_map(img);

############################################ 

is_playing = True
while is_playing:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			is_playing = False

	generate_frame(map)
	frame = pygame.image.load('result.png')
	gameDisplay.fill(map.BLACK)
	gameDisplay.blit(frame, (0, 0))

	pygame.display.update()
	clock.tick(60)

pygame.quit()
quit()


