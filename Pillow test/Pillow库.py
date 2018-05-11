from PIL import Image  # 从PIL库导入Image模块
img = Image.open("c:/234.png")  # 用Image模块的open命令打开指定路径的图片文件
img.show()  # 显示图像
print(img)  # 输出该图片文件的基本信息
print(img.format, img.size, img.height, img.width)
# 制定输出该图片文件的某些指定信息
print(img.getpixel((0, 20)))  # 读取并输出像素值
img.save("acc.jpg")  # 这样写会保存在你py文件所在的路径
img.save("D:/acc.jpg")  # 这样写能保存在你指定的路径
img1 = img.resize((100, 100))
# 将img文件缩放成指定的尺寸 生成为另一个新文件
img1.show()
img1.save("aee.jpg")
img2 = img.rotate(90)  # 将图像逆时针旋转90度
img2.show()  # 查看旋转后的图像
