tz=eval(input("请输入体重(kg)："))#eval
sg=eval(input("请输入身高(m)："))
bmi=tz/(sg*sg)
print("体质指数BMI为：",round(bmi,2))
if bmi<18.5:
    print("过轻")
elif 18.5<=bmi<23.9:
    print("正常")
elif 24<=bmi<27.9:
    print("过重")
elif 28<=bmi<32:
    print("肥胖")
else:
    print("过于肥胖")