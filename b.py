import random
password_len=int(input("请输入密码长度："))
str="abcdefghigklmnopqrsjuvwsyz1234567890!@#$%^&*_+/*";
password="".join(random.sample(str,password_len))
print(password)
# import string
# a=string.ascii_letters+string.digits
# key=[]
# def getKey():
# 	key=random.sample(a,8)
# 	keys="".join(key)
# 	return keys
# for i in range(10):
# 	print(getKey())