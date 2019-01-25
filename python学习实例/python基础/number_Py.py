# numberPy.py

dayup = pow(1.01, 365)
daydown = pow(0.999, 365)
print("向上：{:.2f},向下:{:.2f}".format(dayup, daydown))

# 要用计算机思维，不要用数学思维
# 可以用循环模拟一年的学习，不用求出假日的天数
day = 1.0
dayfactor = 0.01
for i in range(365):
	if i % 7 in [6, 0]:
		day = day * (1 - dayfactor)
	else:
		day = day * (1 + dayfactor)
print("工作日的力量：{:.2f}".format(day))

# 同上，用计算机思维
def dayUP(dayfactor):
	day = 1.0
	for i in range(365):
		if i % 7 in [6, 0]:
			day = day * (1 - dayfactor)
		else:
			day = day * (1 + dayfactor)
	return day

dayfactor = 0.01
while dayUP(dayfactor) < 37.78:
	dayfactor += 0.001
	pass
print("工作日的努力参数是:{:.3f}".format(dayfactor))