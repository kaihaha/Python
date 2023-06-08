numbers = []
while True:
    num = int(input("请输入一个非负整数："))
    if num == -1:
        break
    numbers.append(num)

if len(numbers) == 0:
    print("序列为空")
else:
    print("最大值为：", max(numbers))
    print("最小值为：", min(numbers))
    print("平均值为：", sum(numbers) / len(numbers))