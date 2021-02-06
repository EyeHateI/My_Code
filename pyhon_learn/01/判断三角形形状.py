import math

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
