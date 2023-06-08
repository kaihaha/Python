# import random
# password_len=int(input("请输入密码长度："))
# str="abcdefghigklmnopqrsjuvwsyzQWERTYUIOPASDFGHJKLZXCVBNM1234567890!@#$%^&*_+/*";
# password="".join(random.sample(str,password_len))
# print(password)

# import random
# # 用range()
# def code(len):
#     code_list = []
#     for i in range(10):
#         code_list.append(str(i))  #生成数字
#     for i in range(65, 91):
#         code_list.append(chr(i))   #生成大写字母
#     for i in range(97, 123):
#         code_list.append(chr(i))   #生成小写字母
#     r = random.sample(code_list, len)   
#     m = ''.join(r)
#     return m
# if __name__ == '__main__':
#     n = code(6)
#     print(n)

import random#模块
# 用randint()
code = ''
for i in range(6):#6为随机码
    n = random.randint(0, 9)#数字
    b = chr(random.randint(65, 90))#大写
    s = chr(random.randint(97, 122))#小写
    code += str(random.choice([n, b, s]))#随机选择转换为6位字符串
print(code)#输出出来