n = ''
inputs = []
while n!='N':
    n = input('请输入带有标志(CNY,USD)的钱数:')
    inputs.append(n)
num = len(inputs)
i=0
while i<num:
    b=inputs[i]
    if b[:3] in ['CNY']:
        u = eval(b[3:]) * 0.1424
        print("兑换成USD美元是{:.2f}".format(u),"元")
    elif b[:3] in ['USD']:
        r = eval(b[3:]) * 7.0227
        print("兑换成CNY人民币是{:.2f}".format(r),"元")
    elif b=='N':
        print('')
    else:
        print("输入格式错误")
    i=i+1

# USD = 7.0227
# CNY = 0.1424
# money = input("请输入货币代码和金额(例如USD10或CNY1000):")
# if money[:3] not in ['USD', 'CNY'] or not money[3:].isdigit():
#     print("输入格式错误")
# else:
#     if money[:3] == 'USD': 
#         cny = float(money[3:]) * USD
#         print(f"兑换成人民币是{cny:.2f}元")
#     else: 
#         usd = float(money[3:]) * CNY
#         print(f"兑换成美元是{usd:.2f}元")


# USD = 7.0227
# CNY = 0.1424
# inputs = []
# for i in range(3):
#     n = input('请输入带有标志(CNY,USD)的钱数:')
#     inputs.append(n)
# for n in inputs:
#     if n[:3] in ['CNY']:
#         u = eval(n[3:]) * CNY
#         print("兑换成USD美元是{:.2f}".format(u),"元")
#     elif n[:3] in ['USD']:
#         r = eval(n[3:]) * USD
#         print("兑换成CNY人民币是{:.2f}".format(r),"元")
#     else:
#         print("输入格式错误")