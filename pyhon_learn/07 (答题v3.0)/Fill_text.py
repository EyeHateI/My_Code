class Fill_text:
    n = 1
    key_answer = []
    your_answer = []
    list0 = []
    information = ""
    def __init__(self,name,information):
        self.name = name
        self.information = information
    def TextInfoAdd(list,information):
        Fill_text.information = information
        print(list)
        print()
    def information_judge():                                    #是否查看解析
        c = input("是否查看解析(Y/N):")
        if c == "Y":
            print(Fill_text.information)
            print()
        elif c == "N":
            print("OK")
            print()
    def answer_load(str,list1,list2,list3):                     #答案录入   
        str = input("请输入答案：")
        print()
        list1.append(str)                      
        if list1[0] == list2[0]:                                #进行判断并在list0中输出值
            list3.append(1)                                     #后续会根据list0中输出特定值的个数进行准确率计算
            print("正确")
            print()
            list1.pop(0)
            list2.pop(0)
            Fill_text.information_judge()
        else:
            list3.append(0)
            print("错误")
            print()
            list1.pop(0)
            list2.pop(0)
            Fill_text.information_judge()
    def PrintAll():                                            #一个打印准确率，记录正确与错误题数的方法
        a = Fill_text.list0.count(1)
        b = Fill_text.list0.count(0)
        c = a / Fill_text.n * 100
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
