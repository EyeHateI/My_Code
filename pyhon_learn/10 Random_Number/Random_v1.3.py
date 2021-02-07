'''import random
List = []
for a in range(1,58):
	list.append(a)
print(random.choice(List))
'''
import tkinter as tk
import tkinter.messagebox
import random
import re

def mainGUI():
	window = tk.Tk()
	window.title('random_number_get')
	window.geometry('600x900')
	
	tk.Label(window,text='Range范围').place(x=20,y=20)
	T1 = tk.StringVar(value='')
	tk.Entry(window,textvariable=T1).place(x=20,y=70)
	
	tk.Label(window,text='Num个数').place(x=20,y=120)
	T2 = tk.StringVar(value='')
	tk.Entry(window,textvariable=T2).place(x=20,y=170)
	
	tk.Label(window,text='Request需求').place(x=20,y=220)
	T3 = tk.StringVar(value='')
	tk.Entry(window,textvariable=T3).place(x=20,y=270)
	
	var1 = tk.IntVar()
	tk.Checkbutton(window,text='Re-get允许重复',variable=var1,onvalue=1,offvalue=0).place(x=20,y=320)	
	var2 = tk.IntVar()
	tk.Checkbutton(window,text='特定号码',variable =var2,onvalue=1,offvalue=0).place(x=20,y=360)

	text1 = tk.StringVar()
	info1 = tk.Label(window,textvariable=text1)
	info1.place(x=170,y=70)
	text2 = tk.StringVar()
	info2 = tk.Label(window,textvariable=text2)
	info2.place(x=170,y=170)
	text3 = tk.StringVar()
	info3 = tk.Label(window,textvariable=text3)
	info3.place(x=170,y=270)


	def critic(str,text,info):
		var = 0
		if str == '':
			text.set('× 请输入')
			info['fg'] = 'red'
		else:
			if str.isdigit() == True:
				if int(str) <= 0:
					text.set('× 请输入大于0正整数')
					info['fg'] = 'red'
				else:
					text.set('√')
					info['fg'] = 'green'
					var = 1
			elif str.isdigit() == False:
				text.set('× 请输入大于0的正整数')
				info['fg'] = 'red'	
		return var
		
	
	def Create():
		if (critic(T1.get(),text1,info1) == 1) and (critic(T2.get(),text2,info2) == 1):
			list1 = []
			for num in range(1,int(T1.get())+1):
				list1.append(num)
			list2 = []
			if (int(T1.get()) >= int(T2.get())) and (T3.get() <= T1.get() or T3.get() == ''):	
				while int(T2.get()) > len(list2):
					a = random.choice(list1)
					if int(var2.get()) == 1:
						list2.append(int(T3.get()))
					else:
						if (list2.count(a) >= 1) and (int(var1.get())==1):
							list2.append(a)
						elif list2.count(a) == 0:
							list2.append(a)
				l = tk.Label(window,text='')
				l.place(x=370,y=70)
				l.config(text=list2,width=10,font=('Arial',14),bg='grey')
			else:
				text1.set('× 范围过小')
				info1['fg'] = 'red'		
		else:
			tk.messagebox.showerror(title='Error',message='检查输入!')
	
	tk.Button(window,command=Create,text='get获取',width=13,bg='grey').place(x=50,y=410)
	
	window.mainloop()
	
mainGUI()


#Designed By EyeHateI
