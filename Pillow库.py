from PIL import Image  # 从Pillow库导入Image模块
img = Image.open("c:/123.png")  # 用Image模块的open命令打开指定路径的图片文件
print(img)  # 输出该图片文件的基本信息
print(img.format, img.size)  # 制定输出该图片文件的某些指定信息
