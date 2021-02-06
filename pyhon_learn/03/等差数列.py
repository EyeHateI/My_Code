a1 = float(input("首项a1="))
d = float(input("公差d="))
n = int(input("项数n="))
an = a1+(n-1)*d
Sn = (a1+an)*n/2
if n <= 0:
    print("请输入正确的项数")
a = int(input("求第n项？(输入1确定)"))
if a == 1:
    print(an)
elif a != 1:
    print("OK")
b = int(input("求前n项和Sn?"))
if b == 1:
    print(Sn)
elif b != 1:
    print("OK")
print()

input("按Enter键退出")
