# 目前仅能用于识别大写答案
import requests
import re
import os
import tkinter
import base64
from tkinter.filedialog import askdirectory


def choose_picture():  # 用于选取图片路径
    global path_  # 将path_声明为全局变量 使其在函数外也可以使用
    path_ = tkinter.filedialog.askopenfilename()  # 打开一个文件选取框来选取图片


def ocr():  # 用于文字识别
    url = ("https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic")
    data = {}
    data[
        "access_token"] = "输入你的百度access令牌"
    file = open(path_, "rb")
    image = file.read()
    file.close()

    data["image"] = base64.b64encode(image)
    headers = {
        "Content-Type": "application/x-www-from-urlencoded",
        "apikey": "输入你的APIkey"
    }
    res = requests.post(url=url, headers=headers, data=data)
    result = res.json()
    with open("1.txt", "a") as f:
        for line in result["words_result"]:
            global result1
            result1 = []
            result1.append(line["words"])
            # 创建一个全局变量result1来保存文字识别的结果
            f.write(line["words"] + "\n")
        result1 = str(result1)  # 把list转为str 才可以使用正则表达式


def check_answer():
    p1 = r"[A-Z]"
    pattern1 = re.compile(p1)
    answer = (pattern1.findall(result1))
    key = input("请输入题目的正确答案\n")
    ture_answer = (pattern1.findall(key))
    score = 0
    for x in range(0, len(ture_answer) - 1):
        if (answer[x] == ture_answer[x]):
            score = score + 10
    print("分数为%s" % score)


choose_picture()
ocr()
check_answer()