#-*- coding: UTF-8 -*-
from tkinter import *
from math import *

class AUncertain:
	'''
	求A类不确定度
	'''
	def __init__(self,root):
		'''
		给主窗口赋值
		'''
		self.root = root

	def create(self):
		'''
		窗口，控件的创建
		'''
		# 主窗口创建
		self.root.title('A类不确定度')
		self.root['width']=900
		self.root['height']=600
		self.root.geometry('+495+230')
		self.root.bind('<Return>',self.ok_)
		self.root.resizable(width=False,height=False)
		# 框架1,2创建
		self.frm1=Frame(self.root,width=400,height=600)
		self.frm1.pack(side='left')
		self.frm2=Frame(self.root,width=200,height=250)
		self.frm2.grid_propagate(0)
		self.frm2.pack(side='left')
		# 控件的创建
		self.lat=Label(self.frm1,text='t的值:')
		self.lat.grid(row=0,column=0)
		self.ent=Entry(self.frm1)
		self.ent.grid(row=0,column=1)
		self.ent.focus()
		self.label_count=Label(self.frm1,text='共有几个S:')
		self.label_count.grid(row=1,column=0)
		self.entry_count=Entry(self.frm1)
		self.entry_count.grid(row=1,column=1)
		self.labelNone=Label(self.frm1)
		self.labelNone.grid(row =2)
		Label(self.frm1,text='输入格式如(1.1+2+3):').grid(row=3,column=0,columnspan=2)
		self.text=Entry(self.frm1,width=30)
		self.text.grid(row=4,column=0,columnspan=2)
		self.frmBt=Frame(self.frm1)
		self.frmBt.grid(row=5,column=0,columnspan=2)
		self.bt1=Button(self.frmBt,text='重置',width=7,height=2,command=self.reset_)
		self.bt1.grid(row=0,column=0)
		self.bt2=Button(self.frmBt,text='确定',width=7,height=2)
		self.bt2.grid(row=0,column=1)
		self.bt2.bind('<Button-1>',self.ok_)

	def show(self):
		'''
		显示结果
		'''
		Label(self.frm2).grid(row=1)
		Label(self.frm2).grid(row=2)
		Label(self.frm2).grid(row=3)
		self.labelAver=Label(self.frm2,text='平均值是:')
		self.labelAver.grid(row=4,column=0)
		self.labelAverResult=Label(self.frm2)
		self.labelAverResult.grid(row=4,column=1)
		self.averResult=DoubleVar()
		self.labelAverResult['textvariable']=self.averResult
		self.labelA=Label(self.frm2,text='A类不确定度是:')
		self.labelA.grid(row=5,column=0)
		self.labelAR=Label(self.frm2)
		self.labelAR.grid(row=5,column=1)
		self.aR=DoubleVar()
		self.labelAR['textvariable']=self.aR

	def reset_(self):
		'''
		回调函数，重置按钮
		'''
		self.ent.focus()
		self.averResult.set(0.0)
		self.aR.set(0.0)
		self.ent.delete(0,END)
		self.entry_count.delete(0,END)
		self.text.delete(0,END)
		self.s=0
		self.t=0
		self.sums=0

	def ok_(self,event):
		'''
		回调函数，确定按钮
		'''
		self.t=float(self.ent.get())
		self.sums=int(self.entry_count.get())
		self.s=[]
		string=self.text.get()
		self.s=string.split('+')
		i=0
		sum_=0
		while i<self.sums:
			sum_+=float(self.s[i])
			i+=1
		self.averResult.set(sum_/self.sums)
		i=0
		sum_=0
		while i<self.sums:
			sum_+=pow(self.averResult.get()-float(self.s[i]),2)
			i+=1
		result_=self.t*sqrt(sum_/(self.sums*(self.sums-1)))
		self.aR.set(result_)
		print('平均值是:',self.averResult.get())
		print('A类不确定度是:',self.aR.get())
