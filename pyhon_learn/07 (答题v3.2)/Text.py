import yaml
import sys

f = open('C_T.yaml','r', encoding="utf-8")
list = yaml.load(f)
print(list)
