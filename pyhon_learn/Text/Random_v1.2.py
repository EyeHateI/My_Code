'''import random
List = []
for a in range(1,58):
	list.append(a)
print(random.choice(List))
'''
import tkinter as tk
import tkinter.messagebox
import random

def mainGUI():
	window = tk.Tk()
	window.title('random_number_get')
	window.geometry('200x300')
	
	tk.Label(window,text='Range范围').place(x=20,y=20)
	T1 = tk.StringVar()
	T1.set('')
	tk.Entry(window,textvariable=T1).place(x=20,y=70)
	
	tk.Label(window,text='Num个数').place(x=20,y=120)
	T2 = tk.StringVar()
	T2.set('')
	tk.Entry(window,textvariable=T2).place(x=20,y=170)
	
	def Create():
		list1 = []
		for num in range(1,int(T1.get())+1):
			list1.append(num)
		list2 = []
		while int(T2.get()) > len(list2):
			list2.append(random.choice(list1))
		tk.messagebox.showinfo(title='Info提示',message=list2)
	
	tk.Button(window,command=Create,text='get获取',width=13,bg='grey').place(x=50,y=220)
	
	window.mainloop()
	
mainGUI()


