
class Player:

	def __init__(self, name):
		self.name = name
		self.posx = 0
		self.posy = 0
		self.dir = 0
		self.speed = 0.08

	def move_up(self):
		self.posy -= 0.05

	def move_down(self):
		self.posy += 0.05

	def move_left(self):
		self.posx -= 0.05

	def move_right(self):
		self.posx += 0.05
