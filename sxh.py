#水仙花数
# num = int(input('请输入任意范围，将会得到其范围内的所有水仙花数:'))
# for i in range(1,num+1):
#     cifang = len(str(i))            #这个数的位数，即为次方数
#     total = 0                       #各位数N次方之和
#     j = i                           #因为后面i会用做比较,所以我不更改i的值
#     last_w = 0                      #这个数的最后一位数
#     while j > 0 and cifang > 2:
#         last_w = j % 10             #对10求余，表示这个数的最后一个数
#         j = j // 10                 #去掉最后一位数
#         total += last_w ** cifang   #计算各位的N次方之和
#     if total == i:                  #如果各位数的N次方之后与原数i相等，就打印
#         print(i)


num = int(input('请输入一个三位数:'))
#取百位
i = int(num/100)
i1=int(num//100%10)
#取十位
j = int(num/10%10)
j1=int(num/10%10)
#取个位
k = int(num%10)
result = i*i*i+j*j*j+k*k*k
if result == num:
    print(num,'是水仙花数')
else:
    print(num,'不是水仙花数')