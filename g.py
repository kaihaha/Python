name=eval(input("输入金额："))
rmb1=name//50
name=name%50
rmb2=name//5
name=name%5
rmb3=name
print("金额50元有：",rmb1)
print("金额5元有：",rmb2)
print("金额1元有：",rmb3)