#turtle模块的使用

import turtle
#import turtle as t
#from turtle import *

turtle.setup(650, 350, 200, 200)	#设置窗体大小和位置
turtle.penup()	#画笔升起，移动海龟不画图
turtle.fd(-250)	#前进，forward()函数
turtle.pendown()	#画笔落下
turtle.pensize(25)	#画笔大小或海龟大小，width()
turtle.pencolor("purple")	#画笔颜色
turtle.seth(-40)	#设定海龟朝向，参数是角度，setheading()
for i in range(4):
	turtle.circle(40, 80)	#画圆，以海龟左侧为圆心，第一个参数是半径，第二个是角度
	turtle.circle(-40, 80)	#圆心在右侧
turtle.circle(40, 80/2)
turtle.fd(40)
turtle.circle(16, 180)
turtle.fd(40 * 2/3)
turtle.done()	#程序运行完之后，不会自动退出