import tensorflow as tf

# x = tf.constant([[1.0, 2.0]])
# w = tf.constant([[3.0], [4.0]])
# y = tf.matmul(x, w)
# print(y)
# with tf.Session() as sess:
# 	print(sess.run(y))

##############################

# 前向传播

# # 定义输入和参数
# x = tf.placeholder(tf.float32, shape=(1,2))
# w1 = tf.Variable(tf.random_normal([2,3],stddev=1,seed=1))
# w2 = tf.Variable(tf.random_normal([3,1],stddev=1,seed=1))
# # 定义前向传播过程
# a = tf.matmul(x, w1)
# y = tf.matmul(a, w2)
# # 用会话计算结果
# with tf.Session() as sess:
# 	init_op = tf.global_variables_initializer()
# 	sess.run(init_op)
# 	print("y is:\n",sess.run(y,feed_dict={x:[[0.7,0.5]]}))

# 喂入多组数据

# # 定义输入和参数
# x = tf.placeholder(tf.float32, shape=(None,2))
# w1 = tf.Variable(tf.random_normal([2,3],stddev=1,seed=1))
# w2 = tf.Variable(tf.random_normal([3,1],stddev=1,seed=1))
# # 定义前向传播过程
# a = tf.matmul(x, w1)
# y = tf.matmul(a, w2)
# # 用会话计算结果
# with tf.Session() as sess:
# 	init_op = tf.global_variables_initializer()
# 	sess.run(init_op)
# 	print("y is:\n",sess.run(y,feed_dict={x:[[0.7,0.5],[0.3,0.4],[0.4,0.5]]}))

##############################

# 反向传播

# loss_mse = tf.reduce_mean(tf.square(y - y_))	# 均方误差MSE
# # 反向传播训练方法
# train_step = tf.train.GradientDescentOptimizer(learning_rate).minimize(lose)
# train_step = tf.train.MomentumOptimizer(learning_rate, momentum).minimize(lose)
# train_step = tf.train.AdamOptimizer(learning_rate).minimize(lose)

##############################

# 举例

# 随机产生32组生产出的零件的体积和重量，训练3000轮，每500轮输出一次损失函数。
import numpy as np
BATCH_SIZE = 8
seed = 23455

# 基于seed产生随机数
rng = np.random.RandomState(seed)
# 随机数返回32行2列的矩阵 表示32组 体积和重量 作为输入数据集
X = rng.rand(32,2)
# 从X这个32行2列的矩阵中 取出一行 判断如果和小于1 给Y赋值1 如果和不小于1 给Y赋值0
# 作为输入数据集的标签（正确答案）
Y = [[int(x0 + x1 < 1)] for (x0,x1) in X]
print('X: \n',X)
print('Y: \n',Y)
# 1. 定义神经网络的输入、参数和输出，定义前向传播过程
x = tf.placeholder(tf.float32, shape=[None, 2])
y_ = tf.placeholder(tf.float32, shape=[None, 1])

w1 = tf.Variable(tf.random_normal([2,3],stddev=1,seed=1))
w2 = tf.Variable(tf.random_normal([3,1],stddev=1,seed=1))

a = tf.matmul(x, w1)
y = tf.matmul(a, w2)

# 2. 定义损失函数及反向传播过程
loss = tf.reduce_mean(tf.square(y - y_))
train_step = tf.train.GradientDescentOptimizer(0.001).minimize(loss)
# train_step = tf.train.MomentumOptimizer(0.001,0.9).minimize(loss)
# train_step = tf.train.AdamOptimizer(0.001).minimize(loss)

# 3. 生成会话，训练STEPS轮
with tf.Session() as sess:
	init_op = tf.global_variables_initializer()
	sess.run(init_op)
	# 输出目前（未经训练）的参数值
	print('w1: ',sess.run(w1))
	print('w2: ',sess.run(w2))
	print('\n')

	# 训练模型
	STEPS = 3000
	for i in range(STEPS):
		start = (i*BATCH_SIZE) % 32
		end = start + BATCH_SIZE
		sess.run(train_step,feed_dict={x: X[start:end], y_: Y[start:end]})
		if i % 500 == 0:
			total_loss = sess.run(loss, feed_dict={x: X, y_: Y})
			print('After %d training step(s), loss on all data is %g'%(i,total_loss))
	# 输出训练后的参数取值
	print('\n')
	print('w1: ',sess.run(w1))
	print('w2: ',sess.run(w2))



