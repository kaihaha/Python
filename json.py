import requests
import json
url='https://fanyi.sogou.com/reventondc/suggV3'
ua={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.50'}
data={'kw':'dog'}
response=requests.post(url=url,data=data,headers=ua)
dic_obj=response.json()
fp=open('dog.json','w',encoding='utf-8')
json.dump(dic_obj,fp=fp,ensure_ascii=False)