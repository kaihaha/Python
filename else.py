n = int(input("输入一个正整数n（n>=2）:"))
if n>=2:
    for i in range(2,n):
        if n%i==0:
            print(n,"素数")
            break
    else:
        print(n,"合数") 
else:
    print("错误")