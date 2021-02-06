from Choices_text import *
from Fill_text import *
choices_text.n = 1
list1 = {

}   
choices_text.key_answer = []   
Fill_text.n = 1
    
list2 = {

}
Fill_text.key_answer = []
class Information:
    def __init__(self,n1,n2,k1,k2,list1,list2):
        self.n1 = choices_text.n
        self.list1 = list1
        self.k1 = key_answer
        self.n2 = Fill_text.n
        self.list2 = list2
        self.k2 = Fill_text.key_answer
    def Add():
        if len(list1) >= 1 or len(list2) >= 1:
            print("已手动添加过信息")
            while True:
                a = input("是否将原信息清空[YES/NO]？")
                if a == "YES":
                    dict.clear(list1)
                    break
                elif a == "NO":
                    print("请到info.py中检查并保存信息")
                    break
                else:
                    print("输入有误")
                    continue
        choices_text.n = input("请输入选择题 题数:")
        m1 = [[]]
        n1 = 1
        while n1 <= int(choices_text.n):
            print(f"依次输入第{n1}题信息,")
            print("请输入题干及选项:")
            index0 = 0
            while index0 <= 5:
                if index0 == 1:
                    text = input()
                    list1[f"C{n1}"] = m1
                    m1[0].append(text)
                elif index0 == 2:
                    text = input("A:")
                    list1[f"C{n1}"] = m1
                    m1[0].append(text)
                elif index0 == 3:
                    text = input("B:")
                    list1[f"C{n1}"] = m1
                    m1[0].append(text)
                elif index0 == 4:
                    text = input("C:")
                    list1[f"C{n1}"] = m1
                    m1[0].append(text)
                elif index0 == 5:
                    text = input("D:")
                    list1[f"C{n1}"] = m1
                    m1[0].append(text)
                index0 += 1
            x = input("请输入解析:")
            m1.append(x)
            y = input("请输入答案:")
            choices_text.key_answer.append(y)   
            n1 += 1
        m2 = [[]]
        n2 = 1
        while n2 <= int(choices_text.n):
            print(f"依次输入第{n2}题信息,")
            print("请输入题干:")
            text1 = input()
            list2[f"F{n2}"] = m2
            m2[0].append(text1)
            p = input("请输入解析:")
            m2.append(p)
            q = input("请输入答案:")
            choices_text.key_answer.append(q)   
            n2 += 1
            return ""