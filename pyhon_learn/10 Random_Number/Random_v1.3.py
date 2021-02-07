'''import random
List = []
for a in range(1,58):
	list.append(a)
print(random.choice(List))
'''
import tkinter as tk
import random

def mainGUI():
	window = tk.Tk()
	window.title('random_number_get')
	window.geometry('600x900')
	
	tk.Label(window,text='Range范围').place(x=20,y=20)
	T1 = tk.StringVar()
	T1.set('')
	tk.Entry(window,textvariable=T1).place(x=20,y=70)
	
	tk.Label(window,text='Num个数').place(x=20,y=120)
	T2 = tk.StringVar()
	T2.set('')
	tk.Entry(window,textvariable=T2).place(x=20,y=170)
	
	tk.Label(window,text='Request需求').place(x=20,y=220)
	T3 = tk.StringVar()
	T3.set('')
	tk.Entry(window,textvariable=T3).place(x=20,y=270)
	
	var1 = tk.IntVar()
	tk.Checkbutton(window,text='Re-get允许重复',variable=var1,onvalue=1,offvalue=0).place(x=20,y=320)	
	var2 = tk.IntVar()
	tk.Checkbutton(window,text='特定号码',variable =var2,onvalue=1,offvalue=0).place(x=20,y=360)
	
	def Create():
		list1 = []
		for num in range(1,int(T1.get())+1):
			list1.append(num)
		list2 = []
			
		while int(T2.get()) > len(list2):
			a = random.choice(list1)
			if int(var2.get()) == 1:
				list2.append(int(T3.get()))
			else:
				if (list2.count(a) >= 1) and (int(var1.get())==1):
					list2.append(a)
				elif list2.count(a) == 0:
					list2.append(a)
		l = tk.Label(window,text=''
		'')
		l.place(x=370,y=70)
		l.config(text=list2,width=10,font=('Arial',14))
	
	tk.Button(window,command=Create,text='get获取',width=13,bg='grey').place(x=50,y=410)
	
	window.mainloop()
	
mainGUI()


#Designed By EyeHateI
