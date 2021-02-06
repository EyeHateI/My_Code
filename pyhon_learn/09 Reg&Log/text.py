import hashlib

import re

import tkinter as tk
import tkinter.messagebox

import yaml



def Lock(string):
    password = hashlib.sha256()
    password.update(string.encode())
    passworded = password.digest()
    return passworded
def mainGUI():
    window = tk.Tk()
    window.title('登录')
    window.geometry('480x300')
    least = 5
    length = 12
    

    tk.Label(window,text='登录',font=('Arial',20)).place(x=200,y=0)

    tk.Label(window,text='用户名:',font=('Arial',14)).place(x=50,y=60)
    account = tk.StringVar()
    account.set(f'请输入{least}-{length}位字符')
    e1 = tk.Entry(window,textvariable=account,font=('Arial',14))
    e1.place(x=140,y=60)

    tk.Label(window,text='密码：',font=('Arial',14)).place(x=50,y=100)
    password = tk.StringVar()
    password.set('')
    e2 = tk.Entry(window,textvariable=password,font=('Arial',14),show='*')
    e2.place(x=140,y=100)

    Text = tk.StringVar(window,value='')
    Text.set('')
    info1 = tk.Label(window,textvariable=Text)
    info1.place(x=380,y=60)

    Text2 = tk.StringVar(window,value='')
    Text2.set('')
    info2 = tk.Label(window,textvariable=Text2)
    info2.place(x=380,y=100)

    tk.Label(window,text='Designed by EyeHateI').place(x=40,y=260)

    def login():
        f = open('F:\\360downloads\\python\\WorkPlace\\09 new\\info.yaml','r+',encoding='utf-8')
        a = yaml.safe_load(f)

        if len(account.get()) == 0:
            Text.set('x 请输入账号')
            info1['fg'] = 'Red'
        else:
            Text.set('√')
            info1['fg'] = 'Lime'
            if account.get() in a:
                if len(password.get()) == 0:
                    Text2.set('x 请输入密码!')
                    info2['fg'] = 'Red'
                else:
                    if a[account.get()] == Lock(password.get()):
                        Text2.set('√ 密码正确')     
                        info2['fg'] = 'Lime'             
                        tk.messagebox.showinfo(title='Welcome',message='√ 登录成功!')
                        window.destroy()
                    else:
                        Text2.set('x 密码错误')
                        info2['fg'] = 'Red'
            else:
                Text.set('x 账号不存在')
                info1['fg'] = 'Red'
                b = tk.messagebox.askquestion(title='提示',message='是否前往注册')
                if b == 'yes':
                    sign_up()
                else:
                    pass
            f.close()
    
    tk.Button(window,text='登录',command=login,width=9,bg='grey',font=('Arial',14)).place(x=140,y=140)
    tk.Button(window,text='注册',command=sign_up,width=9,font=('Arial',14)).place(x=250,y=140)
    window.mainloop()
def sign_up():
    window2 = tk.Tk()
    window2.geometry('450x280')
    window2.title('注册')
    tk.Label(window2,text='注册',font=('Arial',20)).place(x=160,y=0)
    tk.Label(window2,text='用户名',font=('Arial',14)).place(x=30,y=40)
    tk.Label(window2,text='密码',font=('Arial',14)).place(x=30,y=80)
    tk.Label(window2,text='确认密码',font=('Arial',14)).place(x=30,y=120)
    
    userName = tk.StringVar(window2,value='')
    userName.set('')
    e3 = tk.Entry(window2,textvariable=userName,show=None,font=('Arial',14),width=17)
    e3.place(x=120,y=40)
    
    U_least = 5
    U_length = 12
    tip1 = tk.Label(window2,text=f'△ 账号长度为{U_least}-{U_length}位字符,仅含字母数字,不含特殊符号',fg='grey',font=('Arial',8))
    tip1.place(x=90,y=64)

    P_w_length = 20
    P_w_least = 6

    tip2 = tk.Label(window2,text=f'△ 密码长度为{P_w_least}-{P_w_length}位字符,可使用@ * _ % .',fg='grey',font=('Arial',8))
    tip2.place(x=90,y=104)
    
    P_w = tk.StringVar(window2,value='')
    e4 = tk.Entry(window2,textvariable=P_w,show='*',font=('Arial',14),width=17)
    e4.place(x=120,y=80)

    P_w2 = tk.StringVar(window2,value='')
    e5 = tk.Entry(window2,textvariable=P_w2,show='*',font=('Arial',14),width=17)
    e5.place(x=120,y=120)

    Text3 = tk.StringVar(window2,value='')
    Text3.set('')
    info3 = tk.Label(window2,textvariable=Text3)
    info3.place(x=310,y=40)
    
    Text4 = tk.StringVar(window2,value='')
    Text4.set('')
    info4 = tk.Label(window2,textvariable=Text4)
    info4.place(x=310,y=80)
    
    Text5 = tk.StringVar(window2,value='')
    Text5.set('')
    info5 = tk.Label(window2,textvariable=Text5)
    info5.place(x=310,y=120)

    def register():
        f1 = open('F:\\360downloads\\python\\WorkPlace\\09 new\\info.yaml','r+',encoding='utf-8')
        a1 = yaml.safe_load(f1)
        dict0 = {}
        if len(userName.get()) == 0:
            Text3.set('x 账号不能为空')
            info3['fg'] = 'red'
        elif len(userName.get()) != 0:
            if str(userName.get()) in a1:
                Text3.set('x 账号已存在')
                info3['fg'] = 'red'
                f1.close
            else:
                if str(userName.get()).isalnum():
                    global least,length
                    if len(userName.get()) < least:
                        Text3.set('x 账号长度过短')
                        info3['fg'] = 'red'
                    elif len(userName.get()) > length:
                        Text3.set('x 账号长度过长')
                        info3['fg'] = 'red'
                    else:
                        Text3.set('√ 账号可用')
                        info3['fg'] = 'lime'
                        if len(P_w.get()) == 0:
                            Text4.set('x 密码不能为空')
                            info4['fg'] = 'red'
                        elif len(P_w.get()) > P_w_length:
                            Text4.set('x 密码长度过长')
                            info4['fg'] = 'red'
                        elif len(P_w.get()) < P_w_least:
                            Text4.set('x 密码长度过短')
                            info4['fg'] = 'red'
                        else:
                            if re.search('^[a-zA-Z0-9@%_.*]{6,20}$',str(P_w.get())) == None:
                                Text4.set('x 密码中含有非法字符')
                                info4['fg'] = 'red'
                            else:
                                Text4.set('√')
                                info4['fg'] = 'lime'

                        if least <= len(P_w.get()) <= length and least <= len(P_w2.get()) <= length:
                            if P_w.get() == P_w2.get():
                                f1.close()
                                f2 = open('F:\\360downloads\\python\\WorkPlace\\09 new\\info.yaml','a+',encoding='utf-8')
                                a2 = yaml.safe_load(f2)
                                dict0[userName.get()] = Lock(P_w2.get())
                                yaml.dump(dict0,f2)
                                f2.close()
                                if tk.messagebox.askquestion(title='Welcome',message='注册成功') == 'yes':
                                    global window
                                    window.destroy()
                                    window2.destroy()
                                    mainGUI()
                                else:
                                    window2.destroy()
                            else:
                                Text5.set('x 两次密码不一致')
                                info5['fg'] = 'red'
                else:
                    Text3.set('x 账号中含有非法字符')
                    info3['fg'] = 'red'
    tk.Button(window2,text='确定',command=register,font=('Arial',14),width=17,bg='grey').place(x=120,y=160)
    window2.mainloop()

mainGUI()

