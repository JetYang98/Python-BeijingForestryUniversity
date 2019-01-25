import win32com.client

class Calculator:
	'''
	装饰器，和播报器的使用
	'''
	def __say(self, word):
		# 会被调用，所以第一个参数为self
		# 只创建一个播报函数，保证以后修改时的方便，不用修改很多处

		# 创将一个播报器对象
		speaker = win32com.client.Dispatch("SAPI.SpVoice")
		# 通过这个播报器对象，直接播放相对应的语音字符串
		speaker.Speak(word)

	def __create_say(word=''):
		'''
		返回一个装饰器
		'''
		def __say_zsq(func):
			def inner(self, n):
				self.__say(word + str(n))
				return func(self, n)
			return inner 
		return __say_zsq 

	def __check_num(func):
		'''
		定义装饰器函数
		'''
		def inner(self, n):
			if not isinstance(n, int):
				raise TypeError('当前类型错误，应为整型')
			return func(self, n)
		return inner

	@__check_num	# 装饰器
	@__create_say()
	def __init__(self, n):
		self.__result = n

	@__check_num
	@__create_say('加')
	def jia(self, n):
		self.__result += n 
		return self

	@__check_num
	@__create_say('减去')
	def jian(self, n):
		self.__result -= n 
		return self

	@__check_num
	@__create_say('乘以')
	def cheng(self, n):
		self.__result *= n 
		return self

	def show(self):
		self.__say('计算结果是：%d' % self.__result)
		print('计算结果是：%d' % self.__result)
		return self

	def clear(self):
		self.__say('清零')
		self.__result = 0
		return self

	@property 	# 将方法转换成属性，属性为只读
	def result(self):
		return self.__result

help(Calculator)
c = Calculator(2)
# help(c)
c.jia(6).jian(4).cheng(5).show().clear().jian(10).show()
print(c.result)
# c.result = 10		# 属性为只读，不可更改