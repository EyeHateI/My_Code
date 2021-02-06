from Choices_text import *
from Fill_text import * 
import yaml
import os

print('一，选择题')
C = open('C_T.yaml','r',encoding='utf-8')     #选择题
list1 = yaml.load(C,Loader=yaml.FullLoader)   #导入题目信息配置
choices_text.n = list1['n']                   #更新题目数量

index1 = 1                                    #题目目录,对题目信息循环读取
while index1 < len(list1):                    #根据题数进行循环
    a = list1[f"C{index1}"]                   #a是指配置文件中 各题的 键 的 列表(键所对应的键值为一个列表)
    choices_text.key_answer.append(a[0][5])   #读取题目答案           a[0]为题干及选项的列表 其中元素依次为题干，ABCD 4个选项,正确答案                                                        
    choices_text.TextInfoAdd(a[0],a[1])       #调用方法 导入 题目信息  a[1]为解析   
    choices_text.answer_load("",choices_text.your_answer,choices_text.key_answer,choices_text.list0)   #导入所有信息 请求终端输入（input）
    index1 += 1               
choices_text.PrintAll()                       #调用打印准确率的方法

print()

print('二，填空题')
F = open("F_T.yaml",'r',encoding='utf-8')  #填空题
list2 = yaml.load(F,Loader=yaml.FullLoader)#导入题目信息配置
Fill_text.n = list2['n']                   #更新题目数量 
                                             
index2 = 1                                 #与选择题代码类似
while index2 < len(list2):
    b = list2[f"F{index2}"]                #b是 配置文件中各题 键 的 列表
    Fill_text.key_answer.append(b[2])      #b[0]为题干 b[1]为解析 b[2]为正确答案
    Fill_text.TextInfoAdd(b[0],b[1])        
    Fill_text.answer_load("",Fill_text.your_answer,Fill_text.key_answer,Fill_text.list0)
    index2 += 1
Fill_text.PrintAll()