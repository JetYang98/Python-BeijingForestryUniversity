class Animal:
	'''
	属性：
		name: str
		age: int
	方法：
		eat(self): 无返回值，打印在吃饭的字符串
		play(self): 无返回值，打印在玩的字符串
		sleep(self): 无返回值，打印在睡觉的字符串
	'''
	def __init__(self, name, age=2):
		self.name = name
		self.age = age
	def eat(self):
		print("%s在吃饭"%self)
	def play(self):
		print("%s在玩"%self)
	def sleep(self):
		print("%s在睡觉"%self)
class Dog(Animal):
	'''
	继承于Animal
	
	方法：
		work(self): 无返回值，打印在看家的字符串
	'''
	def work(self):
		print("%s在看家"%self)
	def __str__(self):
		'''
		调用实例对象时，返回字符串
		'''
		return "姓名为{}，年龄是{}岁的小狗".format(self.name, self.age)
class Cat(Animal):
	'''
	继承于Animal

	方法：
		work(self): 无返回值，打印在捉老鼠的字符串
	'''
	def work(self):
		print("%s在捉老鼠"%self)
	def __str__(self):
		'''
		调用实例对象时，返回字符串
		'''
		return "姓名为{}，年龄是{}岁的小猫".format(self.name, self.age)
class Person(Animal):
	'''
	继承于Animal

	属性：
		pets: list
	方法：
		keep_pets(self): 无返回值，调用宠物的eat(),play(),sleep()函数
		let_pets_work(self): 无返回值，调用宠物的work()函数
	'''
	def __init__(self, name, pets, age=18):
		super(Person, self).__init__(name, age)
		self.pets = pets
	def keep_pets(self):
		for pet in self.pets:
			pet.eat()
			pet.play()
			pet.sleep()
	def let_pets_work(self):
		for pet in self.pets:
			pet.work()
	def __str__(self):
		'''
		调用实例对象时，返回字符串
		'''
		return "姓名为{}，年龄是{}岁的小狗".format(self.name, self.age)

print(__file__)
help(Animal)
help(Dog)
help(Person)
d = Dog('嘟嘟', 5)
c = Cat('小红')
p = Person('小明', [d, c], 20)
p.keep_pets()
p.let_pets_work()