a=int(input("请输入三位正整数："))
x=a//100
y=(a//10)%10
z=a%10
if x>y:
    if x>z:
        a_num=x
    else:
        a_num=z
else:
    if y>z:
        a_num=y
    else:
        a_num=z
print(a,"中数字最大的是：",a_num)