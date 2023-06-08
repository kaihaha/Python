str = input("请输入一句英文:")
u=0
l=0
d=0
for s in str:
    if s.isupper():
        u=u+1
    if s.islower():
        l=l+1
    if s.isdigit():
        d=d+1
print("大写字符:",u)
print("小写字符:",l)
print("数字字符:",d)