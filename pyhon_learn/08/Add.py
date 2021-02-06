import os
import yaml
from Password import *

class info_add:
    dirt = {}
    list = []
    def Add(account,password):
        info_add.dirt[str(account)] = Password.Lock(password)
        curpath = os.path.dirname(os.path.realpath(__file__))
        yamlpath = os.path.join(curpath, "info.yaml")
        f = open(yamlpath,'a+',encoding='utf-8')
        yaml.dump(info_add.dirt,f)
        f.close()
