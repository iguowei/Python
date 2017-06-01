class Animal(object):
	pass

class Runnable(object):
	pass

class Flyable(object):
	pass


	
class Mammal(Animal):
	pass
	
class Bird(Animal):
	def __str__(self):
		return 'this is bird'
	
	__repr__ = __str__
	


class Dog(Mammal):
	pass
	
class Bat(Mammal):
	pass
	

class Parrot(Bird):
	pass
	
class Flyable(Bird):
	pass



class Fib(object):
	def __init__(self):
		self.a, self.b = 0, 1
		
	def __iter__(self):
		return self
		
	def __next__(self):
		self.a, self.b = self.b, self.a + self.b
		if self.a > 20:
			raise NameError()
		return self.a



class demo1(object):
    def __init__(self):
        print("1...")
        self.__name = "demo1"

    def get_name(self):
        return self.__name

    def print(self):
        print(self.__name) # 直接报错
        print(dir(self)) # 查看属性与方法
        print(self._demo2__name) # 有效
        print("1...print...") # 表示执行了该方法

class demo2(object):
    def __init__(self):
        print("2...")
        self.__name = "demo2"

    def get_name(self):
        return self.__name

class demo(demo2,demo1): #和demo1与demo2的顺序有关，demo继承demo2的__name
    pass
    
    
    
def a():
	pass
	
	
	
class Student(object):
	def __init__(self, name):
		self.name = name

	def __call__(self, *args, **kwargs):
		print('My name is %s.' % self.name)
