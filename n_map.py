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
		self.map_w = max(len(l) for l in self.tab)
		self.get_startpos()
		self.complete_map()

	def get_startpos(self):
		posx = self.map_w / 2
		posy = self.map_h / 2
		return posx, posy