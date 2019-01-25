#-*- coding: UTF-8 -*-
from tkinter import *
from math import*

#回调函数
def reset_():                      #重置按钮回调函数
    ent.focus()
    averResult.set(0.0)
    aR.set(0.0)
    ent.delete(0,END)
    entry_count.delete(0,END)
    ens0.delete(0,END)
    ens1.delete(0,END)
    ens2.delete(0,END)
    ens3.delete(0,END)
    ens4.delete(0,END)
    ens5.delete(0,END)
    ens6.delete(0,END)
    ens7.delete(0,END)
    ens8.delete(0,END)
    ens9.delete(0,END)
    s=0
    t=0
    sums=0
    

def ok_(event):                #确定按钮，回车回调函数
    global t
    t=float(ent.get())
    global sums
    sums=int(entry_count.get())
    global s
    s=[]
    s.append(ens0.get())
    s.append(ens1.get())
    s.append(ens2.get())
    s.append(ens3.get())
    s.append(ens4.get())
    s.append(ens5.get())
    s.append(ens6.get())
    s.append(ens7.get())
    s.append(ens8.get())
    s.append(ens9.get())
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
    print('平均值是：',averResult.get())
    print('A类不确定度是：',aR.get())

######################################################
#从此开始#
root=Tk()                         #定义一个根窗口root
root.title('A类不确定度')
root['width']=900
root['height']=600
root.geometry('+480+180')
root.bind('<Return>',ok_)
root.resizable(width=False,height=False)

#框架1,2
frm1=Frame(root,width=450,height=600)                  #输入的框架
##frm1.grid_propagate(0)
frm1.pack(side='left')
frm2=Frame(root,width=200,height=350)                  #输出的框架
frm2.grid_propagate(0)
frm2.pack(side='left')

#t的值,和共有几个s
##frmt=Frame(frm1,width=450,height=40,bg='yellow')                #pack用起来很麻烦
##frmt.pack_propagate(0)          
##frmt.pack(side='top')
lat=Label(frm1,text='t的值:')
##lat.pack(side='left')
lat.grid(row=0,column=0)
ent=Entry(frm1)                                         #t的值
##ent.pack(side='left')
ent.focus()
ent.grid(row=0,column=1)
label_count=Label(frm1,text='共有几个S:')
##label_count.pack()
label_count.grid(row=1,column=0)
entry_count=Entry(frm1)
entry_count.grid(row=1,column=1)
labelNone=Label(frm1)
labelNone.grid(row=2)

#s[10]的值
##frm11=Frame(frm1,width=450,height=20,bg='yellow')
##frm11.pack_propagate(0)
##frm11.pack(side='top')
las0=Label(frm1,text='s[0]的值：')
##la1.pack(side='left')
las0.grid(row=3,column=0)
ens0=Entry(frm1)              #s[0]的值
##en1.pack(side='left')
ens0.grid(row=3,column=1)
##frm12=Frame(frm1,width=450,height=20,bg='yellow')
##frm12.pack_propagate(0)
##frm12.pack(side='top')
las1=Label(frm1,text='s[1]的值：')
##la2.pack(side='left')
las1.grid(row=4,column=0)
ens1=Entry(frm1)         #s[1]的值
##en2.pack(side='left')
ens1.grid(row=4,column=1)
##frm13=Frame(frm1,width=450,height=20,bg='yellow')
##frm13.pack_propagate(0)
##frm13.pack(side='top')
las2=Label(frm1,text='s[2]的值：')
##la3.pack(side='left')
las2.grid(row=5,column=0)
ens2=Entry(frm1)            #s[2]的值
##en3.pack(side='left')
ens2.grid(row=5,column=1)
las3=Label(frm1,text='s[3]的值：')
las3.grid(row=6,column=0)
ens3=Entry(frm1)          
ens3.grid(row=6,column=1)
las4=Label(frm1,text='s[4]的值：')
las4.grid(row=7,column=0)
ens4=Entry(frm1)          
ens4.grid(row=7,column=1)
las5=Label(frm1,text='s[5]的值：')
las5.grid(row=8,column=0)
ens5=Entry(frm1)          
ens5.grid(row=8,column=1)
las6=Label(frm1,text='s[6]的值：')
las6.grid(row=9,column=0)
ens6=Entry(frm1)          
ens6.grid(row=9,column=1)
las7=Label(frm1,text='s[7]的值：')
las7.grid(row=10,column=0)
ens7=Entry(frm1)          
ens7.grid(row=10,column=1)
las8=Label(frm1,text='s[8]的值：')
las8.grid(row=11,column=0)
ens8=Entry(frm1)          
ens8.grid(row=11,column=1)
las9=Label(frm1,text='s[9]的值：')
las9.grid(row=12,column=0)
ens9=Entry(frm1)          
ens9.grid(row=12,column=1)
frmBt=Frame(frm1)
frmBt.grid(row=13,column=0,columnspan=2)
bt1=Button(frmBt,text='重置',width=7,height=2,command=reset_)        #command和bind作用相同
bt1.grid(row=0,column=0)
##bt1.bind("<Button-1>",reset_)
bt2=Button(frmBt,text='确定',width=7,height=2)
bt2.grid(row=0,column=1)
bt2.bind("<Button-1>",ok_)

#显示结果
Label(frm2).grid(row=0)
Label(frm2).grid(row=1)
Label(frm2).grid(row=2)
Label(frm2).grid(row=3)
labelAver=Label(frm2,text='平均值是:')
labelAver.grid(row=4,column=0)
labelAverResult=Label(frm2)
labelAverResult.grid(row=4,column=1)
averResult=DoubleVar()
##averResult.set(12)
labelAverResult['textvariable']=averResult
labelA=Label(frm2,text='A类不确定度是:')
labelA.grid(row=5,column=0)
labelAR=Label(frm2)
labelAR.grid(row=5,column=1)
aR=DoubleVar()
labelAR['textvariable']=aR

root.mainloop()        #消息循环函数
