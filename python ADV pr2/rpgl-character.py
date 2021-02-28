class Dinosaur:
	lives_count = 5
	force = 500	

	def __repr__(self):
		return f'Кол-во жизней: {self.lives_count}, сила: {self.force}'		

dino = Dinosaur()
dino.lives_count = 10
reks = Dinosaur()
print(dino)
print(reks)