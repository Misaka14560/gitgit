import requests
import base64
import ssl, sys
url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic'

data = {}
data['access_token'] = '24.601d6c3ff960b2c51f62ce30960305d1.2592000.1529380639.282335-11267633'

# 读取图片
file = open('F:\TimFiles\接收文件\MobileFile\IMG_20180520_115929.jpg', 'rb')
image = file.read()
file.close()

data['image'] = base64.b64encode(image)
headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "apikey": "Vk8N75dslpKVI512zE6qN9Kr"
}

res = requests.post(url=url, headers=headers, data=data)
result = res.json()
with open("1.txt", "a") as f:
    for line in result["words_result"]:
        print(line["words"], end="")
        f.write(line["words"] + "\n")
