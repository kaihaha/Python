# total = 0
# i = 1
# while i<=100:
#     total += i
#     i += 1
# print("1至100中所有整数的和为：", total)

# 初始化最大值、最小值和总和
# max_num = float('-inf')
# min_num = float('inf')
# total = 0
# count = 0
# # 循环读取输入的数字，直到输入-1
# while True:
#     num = int(input("请输入一个非负整数（输入-1结束）："))
#     if num == -1:
#         break
#     if num >= 0:
#         # 更新最大值、最小值和总和
#         max_num = max(max_num, num)
#         min_num = min(min_num, num)
#         total += num
#         count += 1
# if count > 0:
#     # 计算平均值
#     average = total / count
#     print("最大值为：", max_num)
#     print("最小值为：", min_num)
#     print("平均值为：", average)
# else:
#     print("输入的数字序列为空")



total = 0
count = 0
print("请输入一个非负整数（输入-1结束）")
num = int(input("输入数据:"))
min = num
max = num
while num!=-1:
    count = count+1
    total = total+num
    if num<min:
        min = num
    if num>max:
        max = num
    num = int(input("输入数据:"))
if count>0:
    print("最大{},最小{},平均{:.2f}".format(min,max,total/count))
else:
    print("输入为空")