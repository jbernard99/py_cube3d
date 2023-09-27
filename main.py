import numpy as np
import random as rdm
from math import floor
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
map = map.Map("map.cub", WIDTH, HEIGHT)
player.posx, player.posy = map.get_startpos()

pygame.init()
gameDisplay = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Game')
clock = pygame.time.Clock()

def generate_frame(map):
	img = np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8)
	map.draw_map(img);

generate_frame(map)
frame = pygame.image.load('map.png')
is_playing = True

while is_playing:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			is_playing = False

	keys = pygame.key.get_pressed()
	if keys[pygame.K_UP] or keys[pygame.K_w]:
		player.move_up()
	if keys[pygame.K_DOWN] or keys[pygame.K_s]:
		player.move_down()
	if keys[pygame.K_LEFT] or keys[pygame.K_a]:
		player.move_left()
	if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
		player.move_right()
	
	px = floor(player.posx * map.ss)
	py = floor(player.posy * map.ss)
	print(f"Player : [{px}, {py}]")
	p = pygame.Rect(px, py, 10, 10)
	gameDisplay.fill(map.BLACK)
	gameDisplay.blit(frame, (0, 0))
	pygame.draw.rect(gameDisplay, map.RED, p)

	pygame.display.update()
	clock.tick(60)

pygame.quit()
quit()


