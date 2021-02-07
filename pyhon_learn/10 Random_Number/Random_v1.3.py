'''import random
List = []
for a in range(1,58):
	list.append(a)
print(random.choice(List))
'''
#最初的构思
import tkinter as tk
import tkinter.messagebox
import random

def mainGUI():
	window = tk.Tk()
	window.title('random_number_get')
	window.geometry('600x900')
	#主窗口设置
	tk.Label(window,text='Range范围').place(x=20,y=20)
	T1 = tk.StringVar(value='')
	tk.Entry(window,textvariable=T1).place(x=20,y=70)

	tk.Label(window,text='Num个数').place(x=20,y=120)
	T2 = tk.StringVar(value='')
	tk.Entry(window,textvariable=T2).place(x=20,y=170)
	
	tk.Label(window,text='Request需求').place(x=20,y=220)
	T3 = tk.StringVar(value='')
	tk.Entry(window,textvariable=T3).place(x=20,y=270)
	#输入框1 2 3及相关信息
	var1 = tk.IntVar()
	tk.Checkbutton(window,text='Re-get允许重复',variable=var1,onvalue=1,offvalue=0).place(x=20,y=320)	
	var2 = tk.IntVar()
	tk.Checkbutton(window,text='特定号码',variable =var2,onvalue=1,offvalue=0).place(x=20,y=360)
	#勾选框设置
	text1 = tk.StringVar()
	info1 = tk.Label(window,textvariable=text1)
	info1.place(x=170,y=70)
	text2 = tk.StringVar()
	info2 = tk.Label(window,textvariable=text2)
	info2.place(x=170,y=170)
	text3 = tk.StringVar()
	info3 = tk.Label(window,textvariable=text3)
	info3.place(x=170,y=270)
	#用于判断的提示信息

	def critic(str,text,info):
		var = 0
		if str == '':
			text.set('× 请输入')
			info['fg'] = 'red'
			#判断是否有输入
		else:
			if str.isdigit() == True:
				#判断是否为整数
				if int(str) <= 0:
					text.set('× 请输入大于0正整数')
					info['fg'] = 'red'
					#判断是否为正整数
				else:
					text.set('√')
					info['fg'] = 'green'
					var = 1
			elif str.isdigit() == False:
				text.set('× 请输入大于0的正整数')
				info['fg'] = 'red'	
		return var
		#返回值 方便判断
	
	def Create():
		#主程序函数
		if (critic(T1.get(),text1,info1) == 1) and (critic(T2.get(),text2,info2) == 1):
			#对输入进行初步判断
			list1 = []
			for num in range(1,int(T1.get())+1):
				list1.append(num)
			list2 = []
			#构建包含所有数的列表
			if (int(T1.get()) >= int(T2.get())) and (T3.get() <= T1.get() or T3.get() == ''):
				#判断输入之间的逻辑性关系(是否超出范围)	
				while int(T2.get()) > len(list2):
					a = random.choice(list1)
					#获取随机数
					if int(var2.get()) == 1:
						list2.append(int(T3.get()))
						#获取特定数（非随机）
					else:
						#添加随机数
						if (list2.count(a) >= 1) and (int(var1.get())==1):
							#选择是否存在重复
							list2.append(a)
						elif list2.count(a) == 0:
							list2.append(a)
				l = tk.Label(window,text='')
				l.place(x=370,y=70)
				l.config(text=list2,width=10,font=('Arial',14),bg='grey')
				#结果的输出
			else:
				text1.set('× 范围过小')
				info1['fg'] = 'red'		
		else:
			tk.messagebox.showerror(title='Error',message='检查输入!')
		#一些输入合法性判断
	tk.Button(window,command=Create,text='get获取',width=13,bg='grey').place(x=50,y=410)
	#创建按钮绑定函数
	window.mainloop()
	#主循环
mainGUI()
#运行


#Designed By EyeHateI
