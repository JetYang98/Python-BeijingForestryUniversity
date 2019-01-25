import abc
class Animal(abc.ABC):
	'''
	创建一个抽象类

	也可使用 class Animal(metaclass=abc.ABCMeta)

	方法：
		shout(self): 抽象实例对象函数
		eat(cls): 抽象类对象函数
		play(): 抽象静态函数
	'''
	@abc.abstractmethod
	def shout(self):
		pass
	@abc.abstractclassmethod
	def eat(cls):
		pass
	@abc.abstractstaticmethod
	def play():
		pass
class Dog(Animal):
	'''
	继承于Animal

	实现了3个抽象函数
	'''
	def shout(self):
		print('shout')
	@classmethod
	def eat(cls):
		print('eat')
	@staticmethod
	def play():
		print('play')
# a = Animal()	# 无法初始化一个抽象类
help(Dog)
d = Dog()
d.shout()
d.eat()
d.play()