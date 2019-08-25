# ProgressBar.py

import time
scale = 10
print("执行开始".center(14,'-'))		# 字符居中，用 - 填充
for i in range(scale + 1):
	a = "*" * i
	b = '.' * (scale - i)
	c = (i/scale)*100
	print("{:^3.0f}%[{}->{}]".format(c,a,b))	# 格式化字符串
	time.sleep(0.1)
	pass
print("执行结束".center(14,'-'))

# 单行动态进度条
import time
scale = 50
print("执行开始".center(scale,'-'))
start = time.perf_counter()
for i in range(scale+1):
	a = '*' * i
	b = ' ' * (scale - i)
	c = (i/scale)*100
	dur = time.perf_counter() - start
	print("\r{:^3.0f}%[{}{}]{:.2f}s".format(c,a,b,dur),end='')
	time.sleep(0.1)
print("\n"+"执行结束".center(scale,'-'))