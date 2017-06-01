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
        print(self.__name) # ֱ�ӱ���
        print(dir(self)) # �鿴�����뷽��
        print(self._demo2__name) # ��Ч
        print("1...print...") # ��ʾִ���˸÷���

class demo2(object):
    def __init__(self):
        print("2...")
        self.__name = "demo2"

    def get_name(self):
        return self.__name

class demo(demo2,demo1): #��demo1��demo2��˳���йأ�demo�̳�demo2��__name
    pass
    
    
    
def a():
	pass
	
	
	
class Student(object):
	def __init__(self, name):
		self.name = name

	def __call__(self, *args, **kwargs):
		print('My name is %s.' % self.name)
