from reg_log import *
print("欢迎使用本系统")
print("1.注册 2.登陆")
while True:
    choice = input("请选择：")
    try:
        a = int(choice)
        if a == 1:
            reg_log.register()
            break
        elif a == 2:
            reg_log.login()
            break
        else:
            print("请输入指定序号!".rjust(35))
            continue
    except:
        print("请输入指定序号!".rjust(35))
        continue
"""      
print("1.个人中心")
choice1 = int(input('请选择:'))
"""
