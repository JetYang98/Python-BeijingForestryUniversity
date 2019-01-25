# 递归 ： 函数+分支结构
# 递归链条 + 递归基例
# 汉诺塔例子

class Recursion:
	'''
	利用递归函数解决汉诺塔问题
	'''
	count = 0

	@classmethod
	def hanoi(cls,n,src,dst,mid):
		if n == 1:
			print("{:>2}:{}->{}".format(1,src,dst))
			Recursion.count += 1
		else:
			Recursion.hanoi(n-1,src,mid,dst)
			print("{:>2}:{}->{}".format(n,src,dst))
			Recursion.count += 1
			Recursion.hanoi(n-1,mid,dst,src)
	
