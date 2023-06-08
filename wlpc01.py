# import requests  # 导入requests包
# url = 'https://www.baidu.com/'  # 要访问的网址
# response = requests.get(url)  # 使用get方式发起请求
# html = response.text  # 获取响应的文本
# print(html)

# import requests
# url = 'https://www.baidu.com/img/bd_logo1.png'  # 图片网址
# response = requests.get(url)  # 使用get方式发起请求
# data = response.content  # 获取响应的字节码数据
# with open('baidu_logo.png', 'wb') as f:
#     f.write(data)  # 保存图片

import requests
# 导入requests包
url = 'https://www.baidu.com/'
# 要访问的网址
response = requests.get(url = url)
# 使用get方式发起请求
html = response.text
# 获取响应的文本
print(html)
with open('12950213746.html','w',encoding='utf-8') as fp:
    fp.write(html)