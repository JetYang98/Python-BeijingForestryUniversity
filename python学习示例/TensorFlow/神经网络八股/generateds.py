import numpy as np
import matplotlib.pyplot as plt

BATCH_SIZE = 30
seed = 2

def generateds():
	# 基于seed产生随机数
	rdm = np.random.RandomState(seed)
	X = rdm.randn(300,2)
	Y_ = [int(x0*x0 + x1*x1 < 2) for (x0,x1) in X]	# 是一个1行n列的列表
	Y_c = [['red' if y else 'blue'] for y in Y_]	# 是n行1列的列表

	# print('X is: \n',X)
	# print('Y_ is: \n',Y_)
	# print('Y_c is: \n',Y_c)

	# 对数据集X和Y_进行shape整理，第一个元素为-1表示，随第二个参数计算得到，第二个元素表示多少列，把Y_整理为n行1列。
	# X = np.vstack(X).reshape(-1,2)
	Y_ = np.vstack(Y_).reshape(-1,1)

	# print('X is: \n',X)
	# print('Y_ is: \n',Y_)

	# plt.scatter(X[:,0], X[:,1], c=np.squeeze(Y_c))
	# plt.show()

	return X, Y_, Y_c