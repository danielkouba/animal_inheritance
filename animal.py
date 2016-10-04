class Animal(object):
	def __init__(self, name="animal", health = 100):
		self.name = name
		self.health = health
		self.displayHealth()
	def walk(self):
		if self.health > 1:
			self.health -= 1
			print "Walking..."
		else:
			self.health = 0
			print "Can't Walk Anymore :("
		return self
	def run(self):
		if self.health > 5:
			self.health -=5
			print "Running..."
		else:
			self.health = 0
			print "Can't Run Anymore :("
		return self
	def displayHealth(self):
		print self.name+"'s health is:", self.health

class Dog(Animal):
	def __init__(self,name):
		health = 150
		super(Dog, self).__init__(name, health)
	def pet(self):
		self.health += 5
		print "Petting..."
		return self

class Dragon(Animal):
	def __init__(self,name):
		health = 170
		super(Dragon,self).__init__(name,health)
	def fly(self):
		print "Flying..."
		self.health -= 10
		return self
	def displayHealth(self):
		print "What a dragon!"
		super(Dragon,self).displayHealth()


animal = Animal("Animal")
animal.walk().walk().walk().run().run().displayHealth()


dog = Dog("Fido")
dog.walk().walk().walk().run().run().pet().displayHealth()

dragon = Dragon("Crispy")
dragon.walk().walk().walk().run().run().fly().fly().displayHealth()

# making sure other classes cannot access child's methods
#cat = Animal("Mooshka")
#cat.fly() # AttributeError: 'Animal' object has no attribute 'fly'