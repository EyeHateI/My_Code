import tkinter as tk
from tkinter import  messagebox
import random

window = tk.Tk()
window.geometry('600x900')

def Label_Var(Label,str):
	Label.config(text=str)
	
Frame1 = tk.LabelFrame(window,text='System',padx=100,pady=100)
Frame1.pack(anchor='nw',side='left')
L1 = tk.Label(Frame1,text='?',font=('',10))
L1.pack(anchor='center')

tk.Label(window,text='VS',font=('',10)).place(x=260,y=140)


Frame2 = tk.LabelFrame(window,text='Yours',padx=100,pady=100)
Frame2.pack(anchor='ne',side='right')
L2 = tk.Label(Frame2,text='?',font=('',10))
L2.pack(anchor='center')

list0 = ['石头','剪刀','布']

Yours = ''
System = random.choice(list0)
def Game():
	if Yours == list0[0]:
		if System == list0[1]:
			tk.messagebox.showinfo(message='YouWin')
		elif System == list0[2]:
			tk.messagebox.showinfo(message='YouLost')
		elif System == Yours:
			tk.messagebox.showinfo(message='Dogfall')
	elif Yours == list0[1]:
		if System == list0[2]:
			tk.messagebox.showinfo(message='YouWin')
		elif System == list0[0]:
			tk.messagebox.showinfo(message='YouLost')
		elif System == Yours:
			tk.messagebox.showinfo(message='Dogfall')
	elif Yours == list0[2]:
		if System == list0[0]:
			tk.messagebox.showinfo(message='YouWin')
		elif System == list0[1]:
			tk.messagebox.showinfo(message='YouLost')
		elif System == Yours:
			tk.messagebox.showinfo(message='Dogfall')
	

window.mainloop()