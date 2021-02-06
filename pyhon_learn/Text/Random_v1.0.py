import tkinter as tk
import tkinter.messagebox
import random

def mainGUI():
    window = tk.Tk()
    window.title('随机数获取')
    window.geometry('200x300')

    tk.Label(window,text='随机数范围',font=('Arial',15)).place(x=20,y=20)
    
    T1 = tk.StringVar()
    T1.set('')
    tk.Entry(window,textvariable=T1,font=('Arial',10)).place(x=20,y=50)

    tk.Label(window,text='所需随机数个数',font=('Arial',15)).place(x=20,y=70)

    T2 = tk.StringVar()
    T2.set('')
    tk.Entry(window,textvariable=T2,font=('Arial',10)).place(x=20,y=100)

    def Create():
        list1 = []
        for num in range(1,int(T1.get())+1):
            list1.append(num)
        list2 = []
        while int(T2.get()) > len(list2):
            a = random.choice(list1)
            if list2.count(a) != True:
                list2.append(random.choice(list1))
        tk.messagebox.showinfo(title='提示',message=list2)
    tk.Button(window,command=Create,text='生成',font=('Arial',10),width=13,bg='grey').place(x=50,y=130)
    

    window.mainloop()

mainGUI()