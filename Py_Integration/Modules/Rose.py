# 绘制玫瑰花

import turtle

class Rose:
	'''
	绘制一朵玫瑰花
	'''
	hide = 0
	def __init__(self):
		self.t = turtle.Turtle()
	def degreeCurve(self,n,r,d = 1):
		'''
		定义一个曲线绘制函数
		'''
		self.t.speed(2000)
		for i in range(n):
			self.t.left(d)
			self.t.circle(r,abs(d))

	def init(self):
		'''
		初始位置设定
		'''
		self.s = 0.2		# size
		if Rose.hide == 0:
			self.t.hideturtle()
			Rose.hide = 1
		turtle.setup(450*5*self.s,650*5*self.s)
		self.t.pencolor('black')
		self.t.fillcolor('red')
		self.t.speed(2000)
		self.t.penup()
		self.t.goto(0,900*self.s)
		self.t.pendown()

	def flower(self):
		'''
		绘制花朵形状
		'''
		self.t.speed(2000)
		self.t.begin_fill()
		self.t.circle(200*self.s,30)
		self.degreeCurve(60,50*self.s)
		self.t.circle(200*self.s,30)
		self.degreeCurve(4,100*self.s)
		self.t.circle(200*self.s,50)
		self.degreeCurve(50,50*self.s)
		self.t.circle(350*self.s,65)
		self.degreeCurve(40,70*self.s)
		self.t.circle(150*self.s,50)
		self.degreeCurve(20,50*self.s,-1)
		self.t.circle(400*self.s,60)
		self.degreeCurve(18,50*self.s)
		self.t.fd(250*self.s)
		self.t.right(150)
		self.t.circle(-500*self.s,12)
		self.t.left(140)
		self.t.circle(550*self.s,110)
		self.t.left(27)
		self.t.circle(650*self.s,100)
		self.t.left(130)
		self.t.circle(-300*self.s,20)
		self.t.right(123)
		self.t.circle(220*self.s,57)
		self.t.end_fill()

	def branch(self):
		'''
		绘制花枝形状
		'''
		self.t.speed(2000)
		self.t.left(120)
		self.t.fd(280*self.s)
		self.t.left(115)
		self.t.circle(300*self.s,33)
		self.t.left(180)
		self.t.circle(-300*self.s,33)
		self.degreeCurve(70,225*self.s,-1)
		self.t.circle(350*self.s,104)
		self.t.left(90)
		self.t.circle(200*self.s,105)
		self.t.circle(-500*self.s,63)
		self.t.penup()
		self.t.goto(170*self.s,-30*self.s)
		self.t.pendown()
		self.t.left(160)
		self.degreeCurve(20,2500*self.s)
		self.degreeCurve(220,250*self.s,-1)

	def leaves(self):
		'''
		绘制绿色叶子
		'''
		self.t.speed(2000)
		# 绘制一个绿色叶子
		self.t.fillcolor('green')
		self.t.penup()
		self.t.goto(670*self.s,-180*self.s)
		self.t.pendown()
		self.t.right(140)
		self.t.begin_fill()
		self.t.circle(300*self.s,120)
		self.t.left(60)
		self.t.circle(300*self.s,120)
		self.t.end_fill()
		self.t.penup()
		self.t.goto(180*self.s,-550*self.s)
		self.t.pendown()
		self.t.right(85)
		self.t.circle(600*self.s,40)
		# 绘制另一个绿色叶子
		self.t.penup()
		self.t.goto(-150*self.s,-1000*self.s)
		self.t.pendown()
		self.t.begin_fill()
		self.t.rt(120)
		self.t.circle(300*self.s,115)
		self.t.left(75)
		self.t.circle(300*self.s,100)
		self.t.end_fill()
		self.t.penup()
		self.t.goto(430*self.s,-1070*self.s)
		self.t.pendown()
		self.t.right(30)
		self.t.circle(-600*self.s,35)
		self.t.clear()
	