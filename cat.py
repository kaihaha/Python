import json
import requests
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.50'}
userInput = input("请输入检索内容：")
# 指定url
url='https://fanyi.baidu.com/sug'
# 发出请求，get或post
data={'kw':userInput}
# 获取响应
response = requests.post(url=url,data=data,headers=header)
dic_obj = response.json()
fp=open(userInput + '.json','w',encoding='utf-8')
json.dump(dic_obj,fp=fp,ensure_ascii=False)