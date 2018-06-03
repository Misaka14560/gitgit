import requests
import base64
import re
url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic'

data = {}
data[
    'access_token'] = '24.601d6c3ff960b2c51f62ce30960305d1.2592000.1529380639.282335-11267633'

# 读取图片
file = open('F:\TimFiles\接收文件\9.jpg', 'rb')
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
        result1 = []
        result1.append(line["words"])
        f.write(line["words"] + "\n")
result1 = str(result1)
p1 = r'[A-Z]'
pattern1 = re.compile(p1)
answer=(pattern1.findall(result1))
key=input("请输入正确答案\n")
ture_answer=(pattern1.findall(key))
score=0
for x in range(0,(len(ture_answer))-1):
    if(answer[x]==ture_answer[x]):
        score=score+10
print("分数为%s"%score)        
