# # 模拟登录系统账号密码检测功能
# def login():
#     username = "admin"  # 正确的用户名
#     password = "admin123"  # 正确的密码
#     chances = 3  # 最大尝试次数
#     while True:
#         input_username = input("请输入用户名: ")
#         input_password = input("请输入密码: ")
#         if input_username == username and input_password == password:
#             print("登录成功")
#             break  # 登录成功后结束循环
#         else:
#             chances -= 1
#             print("用户名或密码错误，您还有%d次机会" % chances)
#             if chances == 0:
#                 print("输入错误次数过多，请稍后再试")
#                 break  # 尝试次数用完后结束循环
# # 测试程序
# login()

# 定义账号和密码
username = 'JY2103'
password = '12950213746'
# 定义计数器
count = 0
# 使用while循环，最多尝试3次
while count < 3:
    # 获取用户输入的账号和密码
    input_username = input('请输入账号：')
    input_password = input('请输入密码：')
    # 判断账号和密码是否正确
    if input_username == username and input_password == password:
        print('登录成功！')
        break
    else:
        count += 1
        print('用户名或密码错误，您还有%d次机会' % (3 - count))
# 当用户输入错误超过3次时
if count == 3:
    print('输入错误次数过多，请稍后再试')