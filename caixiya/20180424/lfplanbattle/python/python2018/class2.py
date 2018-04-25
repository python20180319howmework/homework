class Animal(object):
	def run(self):
		print("animal is running")

class Dog(Animal):
	def run(self):
		print("dog is running")

class Cat(Animal):
	def run(self):
		print("cat is running")

	def food(self):
		print("cat likes fish")
ani=Animal()
ani.run()

xiaobai=Dog()
xiaobai.run()

mao=Cat()
mao.run()
mao.food()
