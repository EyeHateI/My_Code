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
        choices_text.information = information                   #list为列表,包含题干,A,B,C,D 5个元素
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
        str = input("请输入答案：")                             #str指用户输入的答案 list1指玩家输入答案汇总后的的列表
        list1.append(str)                                      #list2指正确答案的列表 list3主要是统计正确与错误题数      
        if list1[0] == list2[0]:                               #进行判断并在list3中输出值 1 代表正确 0 代表错误
            list3.append(1)                                    #后续会根据list3中输出特定值(1,0)的个数进行准确率计算
            print("正确")                                      #每次判断后会删除列表list1中的元素 使列表中元素个数始终为1(方便目录读取) 
            print()
            list1.pop(0)
            list2.pop(0) 
            choices_text.information_judge()                   #调用information_judge函数根据输入值判断是否查看解析
        else:
            list3.append(0)
            print("错误")
            print()
            list1.pop(0)
            list2.pop(0)
            choices_text.information_judge()
    def PrintAll():                                            #一个打印准确率，记录正确与错误题数的方法
        a = choices_text.list0.count(1)                        #计算1的个数 代表正确题数
        b = choices_text.list0.count(0)                        #计算0的个数 代表错误题数
        c = a / int(choices_text.n) * 100                      #计算准确率
        print("正确题数:",a)                                    #逐行输出
        print("错误题数:",b)
        print("准确率:",c,"%")
        print()                                                #对准确率进行划分 给予评价
        if c >= 80:
            print("可以啊不错")
        elif c >= 60:
            print("嗯,还行")
        else:
            print("你这不行啊")
