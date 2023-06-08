import random
a=int(input("请输入1-6的正数："))

b=random.randint(1,6)
print("b的随机数：",b)
if a > b:
    print('最大值为',a)
else:
    print('最大值为',b)