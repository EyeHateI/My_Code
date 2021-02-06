import hashlib
import os
import re
import tkinter as tk
import tkinter.messagebox

import yaml

def Lock(string):                                       #对密码进行加密
    password = hashlib.sha256()            
    password.update(string.encode())
    passworded = password.digest()
    return passworded

curpath = os.path.dirname(os.path.realpath(__file__))   #获取当前路径
yamlpath = os.path.join(curpath, "info.yaml")          
n = open(yamlpath,'w+',encoding='utf-8')                #创建名为info.yaml的配置文件
m = yaml.safe_load(n)
dict = {'admin':Lock('123456')}                         #新建默认配置
try:
    m['admin']
except:
    yaml.dump(dict,n)

def mainGUI():                                          #主进程函数
    window = tk.Tk()                                    #主窗口 大小：480x300 标题：登录
    window.title('登录')
    window.geometry('480x300')
    
    tk.Label(window,text='登录',font=('Arial',20)).place(x=200,y=0)  #标签：对界面进行描述

    tk.Label(window,text='用户名:',font=('Arial',14)).place(x=50,y=60)
    least = 5
    length = 12       #账号长度限制
    account = tk.StringVar()
    account.set(f'请输入{least}-{length}位字符')                      #账号输入框
    e1 = tk.Entry(window,textvariable=account,font=('Arial',14))
    e1.place(x=140,y=60)

    tk.Label(window,text='密码：',font=('Arial',14)).place(x=50,y=100)
    password = tk.StringVar()                                        #密码输入框
    password.set('')
    e2 = tk.Entry(window,textvariable=password,font=('Arial',14),show='*')
    e2.place(x=140,y=100)
    #以下为提示信息（账号及密码输入情况）
    Text = tk.StringVar(window,value='')
    Text.set('')                                                     
    info1 = tk.Label(window,textvariable=Text)
    info1.place(x=380,y=60)

    Text2 = tk.StringVar(window,value='')
    Text2.set('')
    info2 = tk.Label(window,textvariable=Text2)
    info2.place(x=380,y=100)
    #小标签hhhh
    tk.Label(window,text='Designed by EyeHateI').place(x=40,y=260)
                                            
    def login():                                        #登录函数            
        f = open(yamlpath,'r+',encoding='utf-8')         
        a = yaml.safe_load(f)                           #读取文件

        if len(account.get()) == 0:                     #判断用户输入
            Text.set('x 请输入账号')                     #账号长度判断
            info1['fg'] = 'Red'
        else:
            if account.get() in a:  #判断账号是否存在
                Text.set('√')       #账号存在则继续输入密码   
                info1['fg'] = 'Lime'
                if len(password.get()) == 0:  #密码是否为空
                    Text2.set('x 请输入密码!')
                    info2['fg'] = 'Red'
                else:                         #密码不为空 继续判断正误
                    if a[account.get()] == Lock(password.get()):
                        Text2.set('√ 密码正确')     
                        info2['fg'] = 'Lime'             
                        tk.messagebox.showinfo(title='Welcome',message='√ 登录成功!')
                        window.destroy()
                    else:
                        Text2.set('x 密码错误')
                        info2['fg'] = 'Red'
            else:                   #账号不存在,提示是否注册
                Text.set('x 账号不存在')
                info1['fg'] = 'Red'
                b = tk.messagebox.askquestion(title='提示',message='是否前往注册')
                if b == 'yes':      #用户判断
                    sign_up()
                else:
                    pass
            f.close()
                
    tk.Button(window,text='登录',command=login,width=9,bg='grey',font=('Arial',14)).place(x=140,y=140)  #登录按钮
    tk.Button(window,text='注册',command=sign_up,width=9,font=('Arial',14)).place(x=250,y=140)          #注册按钮
    window.mainloop()
def sign_up():                #注册函数
    window2 = tk.Tk()         #构建窗口，设置基本参数，显示基本信息
    window2.geometry('450x280')
    window2.title('注册')
    tk.Label(window2,text='注册',font=('Arial',20)).place(x=160,y=0)
    tk.Label(window2,text='用户名',font=('Arial',14)).place(x=30,y=40)
    tk.Label(window2,text='密码',font=('Arial',14)).place(x=30,y=80)
    tk.Label(window2,text='确认密码',font=('Arial',14)).place(x=30,y=120)
    
    userName = tk.StringVar(window2,value='')  #账号输入框
    userName.set('')
    e3 = tk.Entry(window2,textvariable=userName,show=None,font=('Arial',14),width=17)
    e3.place(x=120,y=40)
    
    U_least = 5
    U_length = 12                              #账号长度范围
    tip1 = tk.Label(window2,text=f'△ 账号长度为{U_least}-{U_length}位字符,仅含字母数字,不含特殊符号',fg='grey',font=('Arial',8))
    tip1.place(x=90,y=64)                      #账号规则信息

    P_w_length = 20                            #密码长度范围
    P_w_least = 6

    tip2 = tk.Label(window2,text=f'△ 密码长度为{P_w_least}-{P_w_length}位字符,可使用@ * _ % .',fg='grey',font=('Arial',8))
    tip2.place(x=90,y=104)                     #密码规则信息
    
    P_w = tk.StringVar(window2,value='')       #密码1输入框
    e4 = tk.Entry(window2,textvariable=P_w,show='*',font=('Arial',14),width=17)
    e4.place(x=120,y=80)

    P_w2 = tk.StringVar(window2,value='')      #密码2输入框
    e5 = tk.Entry(window2,textvariable=P_w2,show='*',font=('Arial',14),width=17)
    e5.place(x=120,y=120)

    Text3 = tk.StringVar(window2,value='')     #账号判断提示信息
    Text3.set('')
    info3 = tk.Label(window2,textvariable=Text3)
    info3.place(x=310,y=40) 
    
    Text4 = tk.StringVar(window2,value='')     #密码1提示信息
    Text4.set('')
    info4 = tk.Label(window2,textvariable=Text4)
    info4.place(x=310,y=80)
    
    Text5 = tk.StringVar(window2,value='')     #密码2提示信息
    Text5.set('')
    info5 = tk.Label(window2,textvariable=Text5)
    info5.place(x=310,y=120)

    def register():                            #注册主程序
        f1 = open(yamlpath,'r+',encoding='utf-8')  #以r+模式打开 判断账号是否存在
        a1 = yaml.safe_load(f1)
        dict0 = {}
        if len(userName.get()) == 0:                 #账号是否为空
            Text3.set('x 账号不能为空')
            info3['fg'] = 'red'
        elif len(userName.get()) != 0:           
            if str(userName.get()) in a1:            #账号存在 提示信息
                Text3.set('x 账号已存在')
                info3['fg'] = 'red'
                f1.close
            else:
                if str(userName.get()).isalnum():    #限制账号 只能使用字母数字 str.isalnum()方法 含字母或数字 输出True反之输出False
                    global least,length
                    if len(userName.get()) < U_least:  #账号长度判断
                        Text3.set('x 账号长度过短')
                        info3['fg'] = 'red'
                    elif len(userName.get()) > U_length:
                        Text3.set('x 账号长度过长')
                        info3['fg'] = 'red'
                    else:
                        Text3.set('√ 账号可用')
                        info3['fg'] = 'lime'
                        if len(P_w.get()) == 0:          #密码长度判断
                            Text4.set('x 密码不能为空')
                            info4['fg'] = 'red'
                        elif len(P_w.get()) > P_w_length:
                            Text4.set('x 密码长度过长')
                            info4['fg'] = 'red'
                        elif len(P_w.get()) < P_w_least:
                            Text4.set('x 密码长度过短')
                            info4['fg'] = 'red'
                        else:                            #限制密码 用正则表达式进行匹配
                            if re.search('^[a-zA-Z0-9@%_.*]{6,20}$',str(P_w.get())) == None:
                                Text4.set('x 密码中含有非法字符')
                                info4['fg'] = 'red'
                            else:
                                Text4.set('√')
                                info4['fg'] = 'lime'
                        if P_w_least <= len(P_w.get()) <= P_w_length and P_w_least <= len(P_w2.get()) <= P_w_length:
                            if P_w.get() == P_w2.get():   #判断两次密码是否一致
                                f1.close()                #一致则将加密后的密码添加进配置文件(a+模式)
                                f2 = open(yamlpath,'a+',encoding='utf-8')
                                a2 = yaml.safe_load(f2)
                                dict0[userName.get()] = Lock(P_w2.get())
                                yaml.dump(dict0,f2)
                                f2.close()
                                if tk.messagebox.askquestion(title='Welcome',message='注册成功\n是否前往登录') == 'yes':  
                                    global window                    #注册成功 是否前往登录 对选择进行判断
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
    tk.Button(window2,text='确定',command=register,font=('Arial',14),width=17,bg='grey').place(x=120,y=160)    #确定按钮
    window2.mainloop()      #窗口主循环
mainGUI()                   #运行程序
