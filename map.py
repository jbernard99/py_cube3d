from math import sqrt, floor
from PIL import Image
import time

class Map:

	BLACK = (0,0,0)
	WHITE = (255,255,255)
	GREY = (125,125,125)
	RED = (255,0,0)
	BLUE = (0,25,225)

	def __init__(self, file, i_w, i_h):
		self.tab = []
		self.load_map(file)
		self.img_w = i_w
		self.img_h = i_h
		self.ss = floor((i_h * 0.75) / self.map_h)
		if self.ss > self.img_w / self.map_w:
			print("Map too wide\n")
			input()
			exit()

	def complete_map(self):
		for line in self.tab:
			i = len(line)
			while i < self.map_w:
				line.append(' ')
				i += 1

	def load_map(self, file):
		with open(file, "r") as f:
			txt = f.read()
		for line in txt.split('\n'):
			self.tab.append(list(line))
		self.map_h = len(self.tab)
		max = 0
		for l in self.tab:
			le = len(l)
			if le > max:
				max = le
		self.map_w = max
		self.complete_map()
			
	def tile_by_pixel(self, x, y):
		posx = floor(x / self.ss)
		posy = floor(y / self.ss)
		return self.tab[posy][posx]

	def draw_map(self, img):
		y = 0
		for y in range(0, self.img_h):
			if (y / self.ss <= self.map_h):
				self.draw_map_line(img, y)
		img = Image.fromarray(img, 'RGB')
		img.save('map.png')

	def draw_map_line(self, img, y):
		x = 0
		for x in range(0, self.img_w):
			if (x / self.ss <= self.map_w):
				if (y % self.ss == 0 or x % self.ss == 0):
					img[y, x] = self.BLACK
				else:
					tile = self.tile_by_pixel(x, y)
					if tile == '1':
						img[y, x] = self.GREY
					elif tile == '2':
						img[y, x] = self.BLUE
					elif tile == ' ':
						img[y, x] = self.BLACK
					else:
						img[y, x] = self.WHITE

	def get_startpos(self):
		posx = self.map_w / 2
		posy = self.map_h / 2
		return posx, posy