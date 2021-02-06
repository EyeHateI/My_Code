import yaml
from Add import *
class reg_log:
    def register():
        while True:
            print(repr('<注册>').rjust(12))
            account = Password.account_judge()
            with open('info.yaml','r+',encoding='utf-8') as f:
                a = yaml.safe_load(f)
                try:
                    b = a[account]
                    print("[账号]已被注册,请重新输入")
                    c = input("是否跳转登陆?(Y/N)")
                    if c == 'N':
                        continue
                    elif c == 'Y':
                        reg_log.login()
                        break
                except:
                    keypassword = Password.input_judge("输入[密码]:")
                    while True:
                        re_keypassword = Password.input_judge("确认[密码]:")
                        if keypassword == re_keypassword:
                            info_add.Add(account,keypassword)
                            break
                        else:
                            print(repr('两次密码不一致，请重新输入').rjust(20))
                            continue
                print(repr('注册成功!').rjust(35))
                break
                    
                

    def login():
        while True:
            print(repr('<登陆>').rjust(12))
            account = Password.account_judge()
            f = open('info.yaml','r+',encoding='utf-8')
            a = yaml.safe_load(f)
            try:
                b = a[str(account)]
                Password.True_judge(account)
                print(repr('登录成功').rjust(35))
                break
            except:
                print("[账号]不存在,请重新输入")
                c = input('是否跳转注册?(Y/N)')
                if c == 'N':
                    continue
                elif c == 'Y':
                    reg_log.register()
                    break
