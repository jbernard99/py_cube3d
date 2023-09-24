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

	def draw_map(self, img):
		y = 0

		for y in range(0, self.img_h):
			if (y / self.ss <= self.height):
				self.draw_map_line(img, y)

		img = Image.fromarray(img, 'RGB')
		img.save('result.png')

	def draw_map_line(self, img, y):
		j = 0
		for j in range(0, self.img_w):
			if (y % self.ss == 0):
				img[y, j] = self.BLACK
			else:
				img[y, j] = self.WHITE