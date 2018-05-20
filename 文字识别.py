import requests
import base64
url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic'

data = {}
data['access_token'] = '24.601d6c3ff960b2c51f62ce30960305d1.2592000.1529380639.282335-11267633'

# 读取图片
file = open('F:\TimFiles\接收文件\MobileFile\IMG_20180520_115929.jpg', 'rb')
# "rb"表示以二进制格式打开一个文件用于只读。
# 参考：http://www.runoob.com/python/python-func-open.html
image = file.read()
file.close()
# 打开文件以后要关闭文件，减少内存占用

data['image'] = base64.b64encode(image)  # 用base64将图片数据编码成一串字符串
headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "apikey": "Vk8N75dslpKVI512zE6qN9Kr"
}
# headers参考：https://www.cnblogs.com/yizhenfeng168/p/7078480.html

res = requests.post(url=url, headers=headers, data=data)
result = res.json()
with open("1.txt", "a") as f:
    for line in result["words_result"]:
        print(line["words"], end="")
        f.write(line["words"] + "\n")
