class fill_text:
    n = 1
    key_answer = []
    your_answer = []
    list0 = []
    information = ""
    def __init__(self,name,information):
        self.name = name
        self.information = information
    def TextInfoAdd(list,information):
        fill_text.information = information
        print(list[0])
        print()
    def information_judge():                                    #是否查看解析
        c = input("是否查看解析(Y/N):")
        if c == "Y":
            print(fill_text.information)
            print()
        elif c == "N":
            print("OK")
            print()
    def answer_load(str,list1,list2,list3):                    #答案录入   
        index = 0
        m = 1
        while len(list1) < fill_text.n:
            str = input(f"请输入第{m}题答案：")
            print()
            list1.append(str)
            number1 = len(list1)
            number2 = len(list2)
            if number1 <= number2 + 1:                         #根据输入答案数量与正确答案啊数量对比进行循环输入
                if list1[index] == list2[index]:               #进行判断并在list0中输出值
                    list3.append(1)                            #后续会根据list0中输出特定值的个数进行准确率计算
                    print("正确")
                    print()
                    fill_text.information_judge()
                else:
                    list3.append(0)
                    print("错误")
                    print()
                    fill_text.information_judge()
            index += 1
            m += 1
    def PrintAll():                                            #一个打印准确率，记录正确与错误题数的方法
        a = fill_text.list0.count(1)
        b = fill_text.list0.count(0)
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
                                                                                                                                                                                                                                                                                                                                                                        
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
