# import requests
# word = 'crack'
# url = f'https://fanyi.baidu.com/sug?q={word}'
# response = requests.get(url)
# data = response.json()
# result = []
# for item in data['data']:
#     result.append(item['v'])
# with open('12950213746.txt', 'w', encoding='utf-8') as f:
#     f.write('\n'.join(result))

import requests
import json
url='https://fanyi.baidu.com/sug'
ua={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
data={'kw':'crack'}
response=requests.post(url=url,data=data,headers=ua)
dic_obj=response.json()
fp=open('12950213746.json','w',encoding='utf-8')
json.dump(dic_obj,fp=fp,ensure_ascii=False)