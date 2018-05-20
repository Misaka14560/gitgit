import requests
import ssl, sys
# 获取token
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=【你的APIkey】&client_secret=【你的SK】'
# 填入 自己的APIKEY 和SK
headers = {'Content-Type': 'application/json;charset=UTF-8'}

res = requests.get(url=host, headers=headers).json()
print(res['access_token'])
