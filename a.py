class Student(object):
	def __init__(self, name, age):
		self.__name = name
		self.__age__ = age
	
	def print_score(self):
		print("%s: %s" % (self.__name, self.__age__))
		
	
	def get_name(self):
		return self.__name
		




class Animal(object):
	def run(self):
		print('Animal is running...')
		
		
class Dog(Animal):
	def run(self):
		print("Dog is running...")
		
	def eat(self):
		print('Dog eat meal')
	
class Cat(Animal):
	pass
	
class Other(object):
	def run(self):
		print('so what')
	
	
def run_twice(animal):
	animal.run()
	animal.run()
	


class myObject(object):
	def __init__(self):
		self.name = 'ggg'
		
	def __len__(self):
		return 10
		
		
		
		
class std(object):
	__slots__ = ('name', 'age')
	
	
def set_name(self, name):
	self.__name = name
	
def set_age(self, age):
	self.__age = age
	
	
	
class Std(object):
	@property
	def score(self):
		return self._score
		
	@score.setter
	def score(self, score):
		if not isinstance(score, int):
			raise ValueError('score must be an integer')
	
		if(score<0 or score>100):
			raise ValueError('score must between 0-100')
			
		self._score = score
		
		
	@property
	def age(self):
		return self.__age