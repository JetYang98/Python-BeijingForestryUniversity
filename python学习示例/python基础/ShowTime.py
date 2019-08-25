# 理解方法思维
# 模块化思维：确定模块接口，封装功能
# 规则化思维：抽象过程为规则，计算机自动执行
# 化繁为简：将大功能变为小功能组合，分而治之

import turtle
import time

class ShowTime:
	def __init__(self):
		self.t = turtle.Turtle()
	def drawGap(self):		# 绘制数码管间隔
		self.t.penup()
		self.t.fd(5)
	def drawLine(self,draw):		# 绘制单段数码管
		self.drawGap()
		self.t.pendown() if draw else self.t.penup()
		self.t.fd(40)
		self.drawGap()
		self.t.right(90)
	def drawDigit(self,digit):		# 根据数字绘制七段数码管
		self.drawLine(True) if digit in [2,3,4,5,6,8,9] else self.drawLine(False)
		self.drawLine(True) if digit in [0,1,3,4,5,6,7,8,9] else self.drawLine(False)
		self.drawLine(True) if digit in [0,2,3,5,6,8,9] else self.drawLine(False)
		self.drawLine(True) if digit in [0,2,6,8] else self.drawLine(False)
		self.t.left(90)
		self.drawLine(True) if digit in [0,4,5,6,8,9] else self.drawLine(False)
		self.drawLine(True) if digit in [0,2,3,5,6,7,8,9] else self.drawLine(False)
		self.drawLine(True) if digit in [0,1,2,3,4,7,8,9] else self.drawLine(False)
		self.t.left(180)
		self.t.penup()		# 为绘制后续数字确定位置
		self.t.fd(20)		# 为绘制后续熟悉确定位置
	def drawDate(self,date):		# date为日期，格式为'%Y-%m=%d+'
		self.t.pencolor('red')
		for i in date:
			if i == '-':
				self.t.write('年',font=('Arial',18,'normal'))
				self.t.pencolor('green')
				self.t.fd(40)
			elif i == '=':
				self.t.write('月',font=('Arial',18,'normal'))
				self.t.pencolor("blue")
				self.t.fd(40)
			elif i == '+':
				self.t.write('日',font=("Arial",18,'normal'))
			else:
				self.drawDigit(eval(i))
	def main(self):
		turtle.setup(800,350)
		self.t.penup()
		self.t.fd(-320)
		self.t.pensize(5)
		self.t.hideturtle()
		self.drawDate(time.strftime('%Y-%m=%d+',time.gmtime()))
		turtle.done()

if __name__ == '__main__':
	s = ShowTime()
	s.main()