class Animal(object):
	pass

class Runnable(object):
	pass

class Flyable(object):
	pass


	
class Mammal(Animal):
	pass
	
class Bird(Animal):
	pass
	


class Dog(Mammal):
	pass
	
class Bat(Mammal):
	pass
	

class Parrot(Bird):
	pass
	
class Flyable(Bird):
	pass







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