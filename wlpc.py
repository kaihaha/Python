import requests

url = "https://www.baidu.com/s?wd=requests"
res = requests.get(url=url)

# 获取响应的二进制响应体
content = res.content

# 获取编码后的响应体
html = res.text
# 更改编码格式，需要在text之前设置
res.encoding = "utf-8"

# 获取响应体中的json数据并且反序列化
data = res.json()

# 获取原始响应内容（响应头+响应体）
raw = res.raw
base_data = raw.read()

# 获取响应头
headers = res.headers

# 获取cookie, 类似字典，可以根据字典的方式取值
cookie = res.cookies
print(cookie.get("BIDUPSID"))