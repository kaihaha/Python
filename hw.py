# s = input("输入一个字符串回文:")
# d = s[::-1]
# if d == s:
#     print("是回文")
# else:
#     print("不是回文")

# s = input('请输入一个字符串：')
# a = reversed(list(s))
# if list(a) == list(s):
#     print('是回文')
# else:
#     print('不是回文')

a= int(input("请输入一个四位数："))
q=a//1000
b=a//100%10
h=a//10%10
g=a%10
he=(g*1000)+(h*100)+(b*10)+(q*1)
if he==a:    
    print (a,"是回文数")
elif a!=he:
    print(a,"不是回文数")
else:
    print("请输入一个正确的回文数")
