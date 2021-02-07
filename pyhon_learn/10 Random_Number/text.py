import yaml
import os
curpath = os.path.dirname(os.path.realpath(__file__))   #获取当前路径
yamlpath = os.path.join(curpath, "info.yaml")          
n = open(yamlpath,'r+',encoding='utf-8')                #创建名为info.yaml的配置文件
y = yaml.safe_load(n)
print(len(y))
y.pop(0)
print(list(y))
print(y.count(3))