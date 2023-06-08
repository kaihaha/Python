n=int(input("请输入一个数："))
a,b=0,1
for i in range(n):
    a,b = b,a+b
    print(a)