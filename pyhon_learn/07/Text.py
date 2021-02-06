from tkinter import *
from Choices_text import *
from Fill_text import *
import random
window = Tk()

choices_text.n = 5                                           #在此处输入题号  
key_answer = choices_text.key_answer = ["B","C","B","D","B"]          #在此处输入正确答案
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
Fill_text.PrintAll()
myButton = Button(window,text="下一题")
myButton.pack()
str = ""
def TextAdd(event):
    Text = Label(window,text=str)
    Text.pack()
myButton.bind("<Button-1>",TextAdd)


window.mainloop()