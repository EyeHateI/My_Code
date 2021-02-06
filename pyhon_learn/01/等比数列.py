a1 = float(input("首项="))
q = float(input("公比="))
n = int(input("项数="))
if n <= 0:
    print("请输入正确的项数")
else:
    d = int(input("求第n项？(输入1确定)："))
    if d == 1:
       print(a1*q**(n-1))
    elif d !=1:
       print("OK")

f = int(input("求前n项和？(输入1确定)"))
if f == 1:
    print((a1*(1-q**n))/(1-q))
elif f != 1:
    print("OK")
input("点击enter键退出")