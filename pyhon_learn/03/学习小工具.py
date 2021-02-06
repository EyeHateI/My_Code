print("1.判断三角形形状")
print("2.等差数列")
print("3.等比数列")
print()

Choice = int(input("请输入选项:"))
if Choice == 1:
    a = float(input("较长边a="))
    b = float(input("其余两边b="))
    c = float(input("其余两边c="))
    if a + b < c or a - b > c:
         print("无法构成三角形！")
    else:
        if a**2 == b**2 + c**2:
             print("此三角形是RT△")
        else:
             print("此三角形不是RT△")
    print()
    input("按Enter键退出")
elif Choice == 2:
    a1 = float(input("首项a1="))
    d = float(input("公差d="))
    n = int(input("项数n="))
    an = float(a1+(n-1)*d)
    Sn = float((a1+an)*n/2)
    if n <= 0:
         print("请输入正确的项数")
    a = int(input("求第n项？(输入1确定)"))
    if a == 1:
         print("第",n,"项=",an)
    elif a != 1:
        print("OK")
    b = int(input("求前n项和Sn?(输入1确定)"))
    if b == 1:
        print("前",n,"项和=",Sn)
    elif b != 1:
        print("OK")
    print()
    input("按Enter键退出")
elif Choice == 3:
    a1 = float(input("首项a1="))
    q = float(input("公比q="))
    n = int(input("项数n="))
    an = a1*q**(n-1)
    Sn = a1*(1-q**n)/(1-q)
    if n <= 0:
         print("请输入正确的项数")
    else:
        d = int(input("求第n项？(输入1确定)："))
        if d == 1:
             print("第",n,"项=",an)
        elif d !=1:
             print("OK")
    f = int(input("求前n项和Sn？(输入1确定)"))
    if f == 1:
         print("前",n,"项和=",Sn)
    elif f != 1:
         print("OK")
    print()
    input("点击enter键退出")


