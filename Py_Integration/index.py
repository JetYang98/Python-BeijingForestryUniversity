from Modules import *
from tkinter import *

opList = ['A类不确定度','词云','获取时间','图形显示时间','显示进度条','计算BMI','汉诺塔','玫瑰花']

while True:
	print('*'.center(15,'*'))
	for op in opList:
		print('{:>3}: '.format(opList.index(op)+1) + op)
	print('exit: 退出程序')
	print('*'.center(15,'*') + '\n')
	option = input('请选择功能(输入数字)：')		# 确定选择第几个功能
	print()
	if option == '1':
		tk = Tk()
		aUncert = AUncertain(tk)
		aUncert.create()
		aUncert.show()
		tk.mainloop()
	elif option == '2':
		cm = ChinaMap()
		cm.text()
		cm.word()
		print('词云生成成功!' + '\n')
	elif option == '3':
		Time.getTime()
		print()
	elif option == '4':
		s = ShowTime()
		s.main()
	elif option == '5':
		ProBar.printPro()
		print()
	elif option == '6':
		BMI.getBMI()
		print()
	elif option == '7':
		x = eval(input('有几层塔，请输入数字：'))
		Recursion.hanoi(x,'A','B','C')
		print('一共有{}步'.format(Recursion.count) + '\n')
	elif option == '8':
		r = Rose()
		r.init()
		r.flower()
		r.branch()
		r.leaves()
		print()
	# 退出	
	elif option == 'exit':
		break
	else:
		print('输入有误！')

print('退出成功')
