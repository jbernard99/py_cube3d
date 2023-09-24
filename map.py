from math import sqrt, floor
from PIL import Image
import time

class Map:

	BLACK = (0,0,0)
	WHITE = (255,255,255)

	def __init__(self, m_w, m_h, i_w, i_h):
		self.width = m_w
		self.height = m_h
		self.img_w = i_w
		self.img_h = i_h
		self.ss = 25

	def load_map(self, file):
		with open(file, "r") as f:
			read()

	def draw_map(self, img):
		y = 0
		for y in range(0, self.img_h):
			if (y / self.ss <= self.height):
				self.draw_map_line(img, y)
		img = Image.fromarray(img, 'RGB')
		img.save('result.png')

	def draw_map_line(self, img, y):
		x = 0
		for x in range(0, self.img_w):
			if (x / self.ss <= self.width):
				if (y % self.ss == 0 or x % self.ss == 0):
					img[y, x] = self.BLACK
				else:
					img[y, x] = self.WHITE