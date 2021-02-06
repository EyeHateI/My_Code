import hashlib
import yaml

class Password:
    
    def rule_judge(string):
        len_password = 20
        least_password = 6
        output = 1
        if len(string) > len_password:
            print(f"密码长度超出限制({least_p