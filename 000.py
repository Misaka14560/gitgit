import requests
import os
path1 = os.path.abspath(".")
print(path1)
str(path1)
url = (
    "https://ss2.baidu.com/6ONYsjip0QIZ8tyhnq/it/u=3932680205,4227520103&fm=58"
)
r = requests.get(url)
path = (path1+"/ABC.jpg")
with open(path, "wb") as f:
    f.write(r.content)
f.close()
