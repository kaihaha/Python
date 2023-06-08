# a,b=10,50
# print(a==b)
# if a==b:
#     False
# else:
#     True

import math
a=float(input("请输入三角形边长a:"))
b=float(input("请输入三角形边长b:"))
c=float(input("请输入三角形边长c:"))
# 布尔类型正确或者错误 注意：加":"和缩进
if a+b>c and b+c>a and a+c>b and a>0 and b>0 and c>0:
    h=(a+b+c)/2
    area = math.sqrt(h*(h-a)*(h-b)*(h-c))
    print("三角形的面积为：{:.2f}".format(area))
else:
    print("你输入的边长c,b,a,不构成三角形")

