
class Player:

	def __init__(self, name):
		self.name = name
		self.posx = 0
		self.posy = 0
		self.dir = 0
		self.speed = 0.01

	def move_up(self):
		self.posy -= self.speed

	def move_down(self):
		self.posy += self.speed

	def move_left(self):
		self.posx -= self.speed

	def move_right(self):
		self.posx += self.speed
