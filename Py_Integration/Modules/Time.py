# timePy.py

import time

# pre_t = time.perf_counter()	#获取CPU当前时间

# a = time.time()
# print(a)

# a = time.ctime()
# print(a)

# a = time.gmtime()
# print(a)
class Time:
	'''
	显示日期和时间
	'''
	@classmethod
	def getTime(cls):
		a = time.gmtime()
		b = time.strftime("%Y-%m-%d %A %H:%M:%S",a)
		print(b)	# 方法很好

# a = time.strptime(b,"%Y-%m-%d %A %H:%M:%S")
# print(a)

# time.sleep(0.5)	# 停止0.5秒
# end_t = time.perf_counter()
# t = end_t - pre_t
# print("用了" + str(t) + "秒")