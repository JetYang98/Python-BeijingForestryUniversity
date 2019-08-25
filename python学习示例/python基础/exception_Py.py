# exceptionPy.py

try:
	a = eval(input("请输入数字："))
	print("数字为：{}".format(a))
	pass
except NameError as a:
	print("输入错误")
	print(a)
else:
	print("只有无异常才输出")
	pass
finally:
	print("一定会输出")
	pass