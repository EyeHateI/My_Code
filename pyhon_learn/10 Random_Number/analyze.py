import random
import yaml
import os
list1= []
for a in range(1,58):
    list1.append(a)
T1 = input('抽取个数:')
T2 = input('抽取次数:')

curpath = os.path.dirname(os.path.realpath(__file__))   #获取当前路径
yamlpath = os.path.join(curpath, "info.yaml")          
n = open(yamlpath,'w',encoding='utf-8')                #创建名为info.yaml的配置文件
yaml.dump(list([1]),n)
n.close()
def creator():
    list2 = []
    while int(T1) > len(list2):
        a = random.choice(list1)
        if list2.count(a) != 1:
            list2.append(random.choice(list1))
    f = open(yamlpath,'r+',encoding='utf-8')
    a = yaml.safe_load(f)
    yaml.dump(list2,f)
f1 = open(yamlpath,'r+',encoding='utf-8')
x = yaml.safe_load(f1)
a0 = 0
while int(T2) > a0:
    creator()
    a0 += 1
f1.close()
f2 = open(yamlpath,'r+',encoding='utf-8')
b0 = yaml.safe_load(f2)
b0.pop(0)
for a in range(1,58):
    print(f'{a}的概率:{int(b0.count(a))/(int(T1)*int(T2))*100}%')