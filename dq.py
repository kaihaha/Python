dqbh = input("请输入地区编号:")
sz = int(input("请输入首重:"))
p=0
if sz > 2:
    if dqbh == "01":
        p = 13+3*(sz-2)
    elif dqbh=="02":
        p = 12+2*(sz-2)
    elif dqbh == "03":
        p = 14+4*(sz-2)
elif sz <= 2 and sz>0:
    if dqbh == "01":
            p = 13
    elif dqbh == "02":
            p = 12
    elif dqbh == "03":
            p = 14
if p==0:
    print("错误请重新输入")
else:
    print("您好，此件包裹价格为：",p,"元")