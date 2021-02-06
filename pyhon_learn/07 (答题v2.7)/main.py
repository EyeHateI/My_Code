from Choices_text import *
from Fill_text import *  
from InfoAdd import *
Information.Add()


index1 = 1
while index1 <= len(list1):
    a = list1[f"C{index1}"]
    choices_text.TextInfoAdd(a[0],a[1])
    choices_text.answer_load("",choices_text.your_answer,choices_text.key_answer,choices_text.list0)
    index1 += 1
choices_text.PrintAll()
index2 = 1
while index2 <= len(list2):
    b = list2[f"C{index2}"]
    choices_text.TextInfoAdd(b[0],b[1])
    Fill_text.answer_load("",Fill_text.your_answer,Fill_text.key_answer,Fill_text.list0)
    index2 += 1
Fill_text.PrintAll()
