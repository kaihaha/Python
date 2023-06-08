s = 3
print("您还没有注册，无法登录！")
id = input("请设置账号：")
password = input("请设置密码：")
print("已注册成功！")
print("欢迎来到系统登录界面")
while True:
    ID = input("请输入账号：")
    Password = input("请输入密码：")
    if id == ID and password == Password:
        print("登录成功！")
        break
    elif id == ID:
        print("密码错误！",end="")
        if s !=1:
            print("还有{}次机会".format(s-1))
    elif password == Password:
        print("账号错误！", end="")
        if s != 1:
            print("还有{}次机会".format(s-1))
    else:
        print("账号和密码错误！",end="")
        if s !=1:
            print("还有{}次机会".format(s-1))
    if s<=1:
        print("\n输入次数过多,账号已被冻结！")
        break
    s-=1

# count = 0
# while count < 3:
#     user = input("请输入您的账号：")
#     pwd = input("请输入您的密码：")
#     if user == 'admin' and pwd == '123':
#         print('登录成功')
#         break
#     else:
#         print("用户名或密码错误")
#         count += 1
#         if count == 3:
#             print("输入错误次数过多，请稍后再试")
#         else:
#             print(f"您还有{3-count}次机会")