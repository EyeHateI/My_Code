n = 1 #题数
key_answer1 = ["","","",""]   #选择题答案
key_answer2 = ["","","",""]   #填空题答案
alist0 = []    #选择题准确率统计
blist0 = []    #填空题


#以下为选择题模块
print(".")  #题干
print("A:\nB:\nC:\nD:\n")
A = ""
B = ""
C = ""
D = ""      #选项
list1 = []
list1.append(A)
list1.append(B)
list1.append(C)
list1.append(D)
your_answer = input("你的选项：") #判断正误
if your_answer == key_answer1[1]:
    print("正确!") 
else:
    print("错误,正确答案：",key_answer1[1])   #显示正确选项
    alist0.append("1")
    m = input("是否查看解析(Y/N):")
    if m == "Y":
        print()
        print("解析:")     #注意换行+续行“\n\”
    elif m == "N":        
        print("OK")

#以下为填空题模块
answer1 = input(".")
if answer1 == key_answer2[0]:
    print("正确")
else:
    print("错误，正确答案：",key_answer2[0])
    blist0.append("1")
    m = input("是否查看解析(Y/N):")
    if m == "Y":
        print()
        print("解析:")     #注意换行+续行“\n\”
    elif m == "N":        
        print("OK")