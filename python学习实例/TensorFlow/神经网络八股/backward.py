import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import generateds, forward

STEPS = 40000	# 训练多少次
BATCH_SIZE = 30		# 每次喂养数
LEARNING_RATE_BASE = 0.001	# 学习率基础
LEARNING_RATE_DECAY = 0.99		# 学习率衰减率
REGULARIZER = 0.01		# 正则化

def backward():
	x = tf.placeholder(tf.float32, shape=(None, 2))
	y_ = tf.placeholder(tf.float32, shape=(None, 1))

	X, Y_, Y_c = generateds.generateds()

	y = forward.forward(x,REGULARIZER)

	global_step = tf.Variable(0, trainable=False)	# 记录正在训练第几次
	learning_rate = tf.train.exponential_decay(		# 指数衰减学习率
		LEARNING_RATE_BASE,
		global_step,
		300/BATCH_SIZE,
		LEARNING_RATE_DECAY,
		staircase=True)

	# 定义损失函数
	loss_mse = tf.reduce_mean(tf.square(y-y_))		# 损失函数
	loss_total = loss_mse + tf.add_n(tf.get_collection('losses'))	# 含正则化损失函数

	# 定义反向传播方法：包含正则化
	train_step = tf.train.AdamOptimizer(learning_rate).minimize(loss_total)

	with tf.Session() as sess:
		init_op = tf.global_variables_initializer()		# 初始化变量
		sess.run(init_op)
		for i in range(STEPS):
			start = (i*BATCH_SIZE) % 300
			end = start + BATCH_SIZE
			sess.run(train_step, feed_dict={x: X[start:end], y_: Y_[start:end]})
			if i % 200 == 0:
				loss_v = sess.run(loss_total, feed_dict={x:X, y_:Y_})
				print('After %d steps, loss is: %f'%(i, loss_v))

		# xx在-3到3之间以步长0.01生成网格坐标点
		xx, yy = np.mgrid[-3:3:0.01, -3:3:0.01]
		print("xx is: ",xx)
		# 将xx，yy拉直，合并成一个2列的矩阵
		grid = np.c_[xx.ravel(), yy.ravel()]
		# 将网络指标点喂入神经网络，probs为输出
		probs = sess.run(y, feed_dict={x:grid})
		# 将probs的shape调整成xx的样子
		probs = probs.reshape(xx.shape)
		print("probs is: ",probs)

	# 生成散点图
	plt.scatter(X[:,0],X[:,1],c=np.squeeze(Y_c))
	# 生成轮廓
	plt.contour(xx, yy, probs, levels=[.5])
	plt.show()


if __name__ == '__main__':
	backward()