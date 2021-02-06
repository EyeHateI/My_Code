class choices_text:
    key_answer = []                                 #储存正确答案的列表
    n = 1                                           #题目总数 默认为4
    your_answer = []                                #储存答案的列表
    list0 = []                                      #用于统计的列表
    information = ""                                
    def __init__(self,name,a,b,c,d):                #创建一个方法，对输入信息的读取
        self.name = name
        self.a = A
        self.b = B
        self.c = C
        self.d = D    
    def TextInfoAdd(list,information):                           #创建一个添加信息的方法,主要将信息输入程序
        choices_text.information = information
        print(list[0])
        print("  A:",list[1]) 
        print("  B:",list[2])         
        print("  C:",list[3])  
        print("  D:",list[4])
        return ""
    def information_judge():                                    #是否查看解析
        c = input("是否查看解析(Y/N):")
        print()
        if c == "Y":
            print(choices_text.information)
            print()
        elif c == "N":
            print("OK")
            print()
    def answer_load(str,list1,list2,list3):                    #答案录入   
        str = input("请输入答案：")
        list1.append(str)
        if list1[0] == list2[0]:               #进行判断并在list0中输出值
            list3.append(1)                            #后续会根据list0中输出特定值的个数进行准确率计算
            print("正确")
            print()
            list1.pop(0)
            list2.pop(0)
            choices_text.information_judge()
        else:
            list3.append(0)
            print("错误")
            print()
            list1.pop(0)
            list2.pop(0)
            choices_text.information_judge()
    def PrintAll():                                            #一个打印准确率，记录正确与错误题数的方法
        a = choices_text.list0.count(1)
        b = choices_text.list0.count(0)
        c = a / int(choices_text.n) * 100
        print("正确题数:",a)
        print("错误题数:",b)
        print("准确率:",c,"%")
        print()
        if c >= 80:
            print("可以啊不错")
        elif c >= 60:
            print("嗯,还行")
        else:
            print("你这不行啊")
