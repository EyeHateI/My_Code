from Choices_text import *
from Fill_text import *
choices_text.n = 5                                                              #在此处输入题号  
key_answer = choices_text.key_answer = ["B","C","B","D","B"]                    #在此处输入正确答案
T1 = choices_text.TextInfoAdd(["1. 1 + 1 = ?","1","2","3","4"],"这都不会？？")   #在此处输入各题信息
T2 = choices_text.TextInfoAdd(["2. 2 + 2 = ?","2","3","4","5"],"这都不会？？")   #题目可自行添加
T3 = choices_text.TextInfoAdd(["3. 1 + 2 = ?","2","3","4","5"],"这都不会？？")
T4 = choices_text.TextInfoAdd(["4. 3 + 2 = ?","2","3","4","5"],"这都不会？？")
T5 = choices_text.TextInfoAdd(["5. 4 + 4 = ?","7","8","9","10"],"这都不会？？")
choices_text.answer_load("",choices_text.your_answer,choices_text.key_answer,choices_text.list0)   #题目信息输入
choices_text.PrintAll()                                                                            #打印准确率,输出结果
Fill_text.n = 5
Fill_text.key_answer = ["2","4","3","5","8"]
T1 = Fill_text.TextInfoAdd(["1. 1 + 1 = _____"],"这都不会？？")   #在此处输入各题信息  
T2 = Fill_text.TextInfoAdd(["2. 2 + 2 = _____"],"这都不会？？")   #题目可自行添加
T3 = Fill_text.TextInfoAdd(["3. 1 + 2 = _____"],"这都不会？？")
T4 = Fill_text.TextInfoAdd(["4. 3 + 2 = _____"],"这都不会？？")
T5 = Fill_text.TextInfoAdd(["5. 4 + 4 = _____"],"这都不会？？")
Fill_text.answer_load("",Fill_text.your_answer,Fill_text.key_answer,Fill_text.list0)
Fill_text.PrintAll()                                                                                                                                                                                                                                                                                                                                                                                                                                                                            tringVar()
    P_w.set('')
    e4 = tk.Entry(window2,textvariable=P_w,show='*')
    e4.place(x=140,y=80)

    P_w2 = tk.StringVar()
    P_w2.set('')
    e5 = tk.Entry(window2,textvariable=P_w2,show='*')
    e5.place(x=140,y=120)

    def register():
        f1 = open('info.yaml','a+',encoding='utf-8')
        a1 = yaml.safe_load(f1)
        dict0 = {}
        if Account.account_check(account.get()) == 0:
            try:
                b1 = a1[account]
                tk.messagebox.showinfo(title='提示',message='账号已存在')
            except:
                if P_w.get() == P_w2.get():
                    dict0[account.get()] == password_Lock.Lock(P_w2.get())
                    yaml.dump(dict0,f1)
                    f1.close()
                    tk.messagebox.showinfo(title='Welcome',message='注册成功')
                    window2.destroy()
                else:
                    tk.messagebox.showerror(title='Error',message='两次密码不一致')
        else:
            pass
    
    tk.Button(window2,text='确定',command=register,font=('Arial',14)).place(x=180,y=180)
    window2.mainloop()
window.mainloop()
