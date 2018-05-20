import requests
import base64
url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic'

data = {}
data['access_token'] = '你的百度access_token'

# 读取图片
file = open('你要识别的图片的路径', 'rb')
# "rb"表示以二进制格式打开一个文件用于只读。
# 参考：http://www.runoob.com/python/python-func-open.html
image = file.read()
file.close()
# 打开文件以后要关闭文件，减少内存占用

data['image'] = base64.b64encode(image)  # 用base64将图片数据编码成一串字符串
headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "apikey": "你的百度APIkey"
}
# headers参考：https://www.cnblogs.com/yizhenfeng168/p/7078480.html

res = requests.post(url=url, headers=headers, data=data)
result = res.json()
with open("1.txt", "a") as f:
    for line in result["words_result"]:
        print(line["words"], end="")
        f.write(line["words"] + "\n")
