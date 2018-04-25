class Person():
	#__slots__=("_birth","name")
	@property
	def birthday(self):
		return self._birthday
	@birthday.setter
	def birthday(self,value):
		self._birthday=value

	@property
	def age(self):
		return 2018-self._birthday
p=Person()
p.birthday=1996
print(p.birthday)
print(p.age)	
p.name="cai"
print(p.name)
p.age=20
print(p.age)	
