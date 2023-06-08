odd = 0
even = 0
for i in range(1,101):
    if i%2 == 1:
        odd = odd+i
    else:
        even = even+i
print("奇数:",odd)
print("偶数:",even)

print('使用for循环计算1到100之间的奇数和')
sum=0 #用于存储偶数和
for item in range(1,101):
    if item %2!=0:
        sum+=item
print('1到100之间的奇数和为:',sum)

print('使用for循环计算1到100之间的偶数和')
sum=0 #用于存储偶数和
for item in range(1,101):
    if item %2==0:
        sum+=item

print('1到100之间的偶数和为:',sum)