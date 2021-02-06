import hashlib
import yaml

class Password:
    
    def rule_judge(string):
        len_password = 20
        least_password = 6
        output = 1
        if len(string) > len_password:
            print(f"密码长度超出限制({least_password}-{len_password})")
            print('请重新输入')
            output = 2
        elif len(string) < least_password:
            print(f'密码长度过短({least_password}-{len_password})')
            print('请重新输入')
            output = 2
        elif str(string).isalnum == True:
            pass
        elif str(string).isalnum == False:
            print("密码中含有非法字符")
            print('请重新输入')
            output = 2
        else:
            pass
        return output
    def input_judge(string):
        while True:
            password = input(str(string))
            text = Password.rule_judge(password)
            if text == 1:
                break
            elif text == 2:
                continue
        return password
    
    def account_judge():
        length_all = 12
        length_least = 5
        while True:
            account = input("请输入账号:")
            if str(account).isalnum == True:
                print("账号内含有非法字符".rjust(35))
                break
            elif length_least <= len(str(account)) <= length_all:
                print("账号可用.".rjust(35))
                break
            elif len(str(account)) < length_least or len(str(account)) > length_all:
                print(f"请输入{length_least}-{length_all}位字符!".rjust(35))
                continue
            else:
                continue
        return account
    def Lock(string):
        password = hashlib.sha256()
        password.update(string.encode())
        Pw_Lock = password.digest()
        return Pw_Lock
    
    def True_judge(account):
        f = open('info.yaml','r+',encoding='utf-8')
        keypassword_file = yaml.safe_load(f)
        keypassword = keypassword_file[account]
        while True:
            yourpassword = Password.input_judge('请输入[密码]')
            if Password.Lock(yourpassword) == keypassword:
                print('密码正确'.rjust(35))
                break
            else:
                print('密码错误!请检查输入'.rjust(35))
                continue
        f.close()
    """
    def password_change(account):
        print("请输入初始密码")
        Password.password_judge(account)
        Password_ed = Password.Lock(input("请输入修改后的密码:"))
        f = open('info.yaml','r+',encoding='utf-8')
        keypassword_file = yaml.safe_load(f)
        keypassword_file[account] = Password_ed
        print("修改成功")
    """