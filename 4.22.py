# for a in range(1, 10):
#     for b in range(1, a + 1):
#         print(a, "*", b, "=", a * b, end=" ")
#     print("\t")
import requests
from bs4 import BeautifulSoup
r = requests.get("http://python123.io/ws/demo.html")
r.text
demo = r.text
# from bs4 import BeautifulSoup
soup = BeautifulSoup(demo, "html.parser")
soup.title
tag = soup.a
print(tag)
print(soup.a.name)
print(soup.a.parent.name)
print(soup.a.parent.parent.name)
print(tag.attrs)
print(tag.attrs["class"])
print(tag.attrs["href"], "\t", type(tag.attrs), "\t", type(tag))
