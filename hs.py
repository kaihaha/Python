# n = int(input("输入一个正整数n（n>=2）:"))
# if n>=2:
#     for i in range(2,n):
#         if n%i==0:
#             break
#     if i==n-1:
#         print(n,"素数")
#     else:
#         print(n,"合数") 
# else:
#     print("错误")

n = int(input("请输入一个正整数n（n>=2）："))
if n < 2:
    print("不是素数")
else:
    prime = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            prime = False
            continue
    if prime:
        print("是素数")
    else:
        print("不是素数")