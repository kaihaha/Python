x=eval(input("请输入x长度："))
y=eval(input("请输入y长度："))
z=eval(input("请输入z长度："))
#三角形周长
q=(x+y+z)/2
print("三角形周长为：",q)
#三角形面积
S=(q*(q-x)*(q-y)*(q-z))**0.5
print("三角形面积为：%0.1f"%S)