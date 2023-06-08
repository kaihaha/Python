def digui(n):
    if n==0:
        return 1
    else:
        return n*digui(n-1)
num = eval(input("请输入一个正整数:"))
print(digui(num))