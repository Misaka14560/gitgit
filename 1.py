import requests
r=requests.get("https://www.baidu.com/s?ie=UTF-8&wd=http%E7%8A%B6%E6%80%81%E7%A0%81%E5%A4%A7%E5%85%A8")
print(r.text)