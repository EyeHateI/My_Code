class choices_text:
    key_answer = []                                 #储存正确答案的列表
    n = 1                                           #题目总数 默认为4
    your_answer = []                                #储存答案的列表
    list0 = []                                      #用于统计的列表
    information = ""                                
    def __init__(self,name,a,b,c,d):                #创建一个方法，对输入信息的读取
        self.name = name
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    def TextInfoAdd(self,list,information):                           #创建一个添加信息的方法,主要将信息输入程序
        choices_text.information = information
        print(list[0])
        print("  A:",list[1]) 
        print("  B:",list[2])         
        print("  C:",list[3])  
        print("  D:",list[4])
        return ""
    def information_judge(self):                                    #是否查看解析
        c = input("是否查看解析(Y/N):")
        print()
        if c == "Y":
            print(choices_text.information)
            print()
        elif c == "N":
            print("OK")
            print()
    def answer_load(self,str,list1,list2,list3):                    #答案录入   
        index = 0
        m = 1
        while len(list1) < choices_text.n:
            str = input(f"请输入第{m}题答案：")
            list1.append(str)
            number1 = len(list1)
            number2 = len(list2)
            if number1 <= number2 + 1:                         #根据输入答案数量与正确答案啊数量对比进行循环输入
                if list1[index] == list2[index]:               #进行判断并在list0中输出值
                    list3.append(1)                            #后续会根据list0中输出特定�