Text_number = 5  #题数
key_answer = ["D","D","B","B","A"]#正确答案
list0 = []    #准确率统计

print("1.已知数列{an}满足an+1=3an，且a2•a4•a6=9，则log3 a5+log3 a7+log3 a9=（　　）")  #题干
print("A:5\nB:6\nC:8\nD:11\n")
A = "5"
B = "6"
C = "8"
D = "11"      #选项
list1 = []
list1.append(A)
list1.append(B)
list1.append(C)
list1.append(D)
your_answer = input("你的选项：") #判断正误
if your_answer == key_answer[0]:
    print("正确!") 
else:
    print("错误,正确答案：",key_answer[0])#显示正确选项
    list0.append("1")
    m = input("是否查看解析(Y/N):")
    if m == "Y":
        print()
        print("解析:\n\
        根据题意，分析可得:\n\
        数列{an}为等比数列，且其公比q=3，由等比数列的性质可得（a4）3=a2•a4•a6=9，结合对数的运算性质即可得答案．\n\
        解：根据题意，数列{an}满足an+1=3an，则数列{an}为等比数列，且其公比q=3，\n\
        若a2•a4•a6=9，则（a4）3=a2•a4•a6=9，\n\
        则log3a5+log3a7+log3a9=log3（a5•a7•a9）=log3（a7）3=log3（a4q3）3=11；\n\
        故选：D．")
    elif m == "N":
        print("OK")


print("2.在等比数列{an}中，已知a1＝1，(a5+a7)/(a2+a4)=1/8,则a5的值为（ ）")  #题干
print("A:1/2\nB:1/4\nC:1/8\nD:1/16\n")
A = "1/2"
B = "1/4"
C = "1/8"
D = "1/16"      #选项
list2 = []
list2.append(A)
list2.append(B)
list2.append(C)
list2.append(D)
your_answer = input("你的选项：") #判断正误
if your_answer == key_answer[1]:
    print("正确!") 
else:
    print("错误,正确答案：",key_answer[1])#显示正确选项
    list0.append("1")
    m = input("是否查看解析(Y/N):")
    if m == "Y":
        print()
        print("解析:利用等比数列的通项公式求出公比，由此能求出a5的值．\n\
        解：在等比数列{an}中，\n\
        ∵a1＝1，\n\
        (a5+a7)/(a2+a4)＝1/8，\n\
        ∴(q^4+q^6)/(q+q^3)=1/8，\n\
        解得q=1/2，\n\
        ∴a5=q4=1/16．\n\
        故选：D．")     #注意换行+续行“\n\”
    elif m == "N":        
        print("OK")


print("3.2. 已知等比数列{an}满足a1=3，a1+a3+a5=21，则a3+a5+a7=（　　）")  #题干
print("A:21\nB:42\nC:63\nD:84\n")
A = "21"
B = "42"
C = "63"
D = "84"      #选项
list3 = []
list3.append(A)
list3.append(B)
list3.append(C)
list3.append(D)
your_answer = input("你的选项：") #判断正误
if your_answer == key_answer[2]:
    print("正确!") 
else:
    print("错误,正确答案：",key_answer[2])#显示正确选项
    list0.append("1")
    m = input("是否查看解析(Y/N):")
    if m == "Y":
        print()
        print("解析:由已知，a1=3，a1+a3+a5=21，利用等比数列的通项公式可求q，然后在代入等比数列通项公式即可求．\n\
        解:∵a1=3，a1+a3+a5=21，\n\
           ∴a1(1+q2+q4)＝21，\n\
           ∴q4+q2+1=7，\n\
           ∴q4+q2-6=0，\n\
           ∴q2=2，\n\
           ∴a3+a5+a7=a1(q2+q4+q6)=3×（2+4+8）=42．\n\
        故选：B．")     #注意换行+续行“\n\”
    elif m == "N":        
        print("OK")

print("4.在等比数列{an}中，a2，a18是方程x^2+6x+4=0的两根，则a4•a16+a10=（　　）")  #题干
print("A:6\nB:2\nC:2或6\nD:-2\n")
A = "6"
B = "2"
C = "2或6"
D = "-2"      #选项
list4 = []
list4.append(A)
list4.append(B)
list4.append(C)
list4.append(D)
your_answer = input("你的选项：") #判断正误
if your_answer == key_answer[3]:
    print("正确!") 
else:
    print("错误,正确答案：",key_answer[3])#显示正确选项
    list0.append("1")
    m = input("是否查看解析(Y/N):")
    if m == "Y":
        print()
        print("解析:根据等比数列的性质，利用根与系数的关系，即可得出正确的结论．\n\
        解：等比数列{an}中，a2，a18是方程x^2+6x+4=0的两根，\n\
            ∴a2•a18=4，且a2+a18=-6，\n\
            ∴a2＜0，且a18＜0，\n\
            ∴a10＜0\n\
            ∴a4•a16=a2•a18=4，(a10)^2=a2•a18=4，\n\
            ∴a10=-2，\n\
            ∴a4•a16+a10=4-2=2\n\
        故选：B．")     #注意换行+续行“\n\”
    elif m == "N":        
        print("OK")


print("5. 等比数列x，3x+3，6x+6，…的第四项等于（　　）")  #题干
print("A:-24\nB:0\nC:12\nD:24\n")
A = "-24"
B = "0"
C = "12"
D = "24"      #选项
list5 = []
list5.append(A)
list5.append(B)
list5.append(C)
list5.append(D)
your_answer = input("你的选项：") #判断正误
if your_answer == key_answer[4]:
    print("正确!") 
else:
    print("错误,正确答案：",key_answer[4])#显示正确选项
    list0.append("1")
    m = input("是否查看解析(Y/N):")
    if m == "Y":
        print()
        print("解析:由题意可得（3x+3）2=x（6x+6），解x的值，可得此等比数列的前三项，从而求得此等比数列的公比，从而求得第四项．\n\
        解：由于 x，3x+3，6x+6是等比数列的前三项，故有（3x+3）2=x（6x+6），解x=-3，\n\
        故此等比数列的前三项分别为-3，-6，-12，故此等比数列的公比为2，故第四项为-24，\n\
        故选：A．")     #注意换行+续行“\n\”
    elif m == "N":        
        print("OK")


Mistake_nuber = list0.count("1")    #错误题数
print("准确率：",100-Mistake_nuber/Text_number*100,"%")  #计算准确率