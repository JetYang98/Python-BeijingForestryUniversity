#-*- coding: UTF-8 -*-
from tkinter import *
from math import *

#回调函数
def reset_():
        ent.focus()
        averResult.set(0.0)
        aR.set(0.0)
        ent.delete(0,END)
        entry_count.delete(0,END)
        text.delete(0,END)
        s=0
        t=0
        sums=0
	
	
def ok_(event):
	global t
	t=float(ent.get())
	global sums
	sums=int(entry_count.get())
	global s
	s=[]
	string=text.get()
	s=string.split('+')
	i=0
	sum_=0
	while i<sums:
		sum_+=float(s[i])
		i+=1
	averResult.set(sum_/sums)
	i=0
	sum_=0
	while i<sums:
		sum_+=pow(averResult.get()-float(s[i]),2)
		i+=1
	result_=t*sqrt(sum_/(sums*(sums-1)))
	aR.set(result_)
	print('平均值是:',averResult.get())
	print('A类不确定度是:',aR.get())
	
################################################################
#从此开始#
root=Tk()
root.title('A类不确定度')
root['width']=900
root['height']=600
root.geometry('+495+230')
root.bind('<Return>',ok_)
root.resizable(width=False,height=False)

#框架1,2
frm1=Frame(root,width=400,height=600)
frm1.pack(side='left')
frm2=Frame(root,width=200,height=250)
frm2.grid_propagate(0)
frm2.pack(side='left')

#t的值，和共有几个s
lat=Label(frm1,text='t的值:')
lat.grid(row=0,column=0)
ent=Entry(frm1)
ent.grid(row=0,column=1)
ent.focus()
label_count=Label(frm1,text='共有几个S:')
label_count.grid(row=1,column=0)
entry_count=Entry(frm1)
entry_count.grid(row=1,column=1)
labelNone=Label(frm1)
labelNone.grid(row =2)

Label(frm1,text='输入格式如(1.1+2+3):').grid(row=3,column=0,columnspan=2)
text=Entry(frm1,width=30)
text.grid(row=4,column=0,columnspan=2)
frmBt=Frame(frm1)
frmBt.grid(row=5,column=0,columnspan=2)
bt1=Button(frmBt,text='重置',width=7,height=2,command=reset_)
bt1.grid(row=0,column=0)
##bt1.bind('<Button-1>',reset_)
bt2=Button(frmBt,text='确定',width=7,height=2)
bt2.grid(row=0,column=1)
bt2.bind('<Button-1>',ok_)

#显示结果
Label(frm2).grid(row=1)
Label(frm2).grid(row=2)
Label(frm2).grid(row=3)
labelAver=Label(frm2,text='平均值是:')
labelAver.grid(row=4,column=0)
labelAverResult=Label(frm2)
labelAverResult.grid(row=4,column=1)
averResult=DoubleVar()
labelAverResult['textvariable']=averResult
labelA=Label(frm2,text='A类不确定度是:')
labelA.grid(row=5,column=0)
labelAR=Label(frm2)
labelAR.grid(row=5,column=1)
aR=DoubleVar()
labelAR['textvariable']=aR

root.mainloop()          #消息循环函数
