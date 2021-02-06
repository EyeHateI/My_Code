#小游戏：石头剪刀布
import random
list = ["石头","剪刀","布"]  #指定输入内容
choice0 = False
list0 = []                  #统计胜率
def judge(str):                         #定义judge函数对结果进行判断
    if str == "win":
        print("系统：",system,end="  ")
        print()
        print("你赢了")
        list0.append(1)
    elif str == "lost":
        print("系统：",system,end="  ")
        print()
        print("你输了")
        list0.append(-1)
    elif str == "neither":
        print("系统：",system,end="  ")
        print()
        print("平局")
        list0.append(0)
    return
while choice0 == False:#游戏循环
    player = input("你的选择：")        #玩家选择
    system = random.choice(list)       #系统随机选择
    a = player in list                 #对玩家选择进行判断
    if a == False:
        print("输入有误")
        choice2 = input("重新输入？(Enter继续,输入N退出)")
        if choice2 == "":
            print()
            continue
        elif choice2 == "N":
            print()
            break
    else:                              #判断胜负
        if player == list[0]:
            if system == list[1]:
                judge("win")
            elif system == list[2]:
                judge("lost")
            else:
                judge("neither")
        elif player == list[1]:
            if system == list[2]:
                judge("win")
            elif system == list[0]:
                judge("lost")
            else:
                judge("neither")
        else:
            if system == list[0]:
                judge("win")
            elif system == list[1]:
                judge("lost")
            else:
                judge("neither")
        print()                        #玩家的二次选择
        choice = input("是否继续?(Enter继续,输入E退出):")
        print()
        if choice == "":
            choic0 = False
        elif choice == "E":
            choice0 = True
print()                                #统计胜率进行输出
print("您共玩了",len(list0),"局")
print("胜:",list0.count(1))
print("平:",list0.count(0))
print("败:",list0.count(-1))