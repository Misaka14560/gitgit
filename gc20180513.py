import PIL.Image as Image
import itchat
import os
import math
itchat.auto_login()
friends = itchat.get_friends(update=True)[0:]
user = friends[0]['UserName']
num = 0
for i in friends:
    print('donnloading NO.' + str(num + 1) + " image")
    img = itchat.get_head_img(userName=i["UserName"])
    fileImage = open("avatar" + "/" + str(num) + ".jpg", "wb")
    fileImage.write(img)
    fileImage.close()
    num += 1

Is = os.listdir("avatar")
each_size = int(math.sqrt(float(640 * 640) / len(Is)))
lines = int(640 / each_size)
image = Image.new("RGBA", (640, 640))

x = 0
y = 0
for i in range(0, len(Is) - 1):
    try:
        img = Image.open("avatar" + "/" + str(i) + ".jpg")
    except IOError:
        print("error")
    else:
        img = img.resize((each_size, each_size), Image.ANTIALIAS)
        image.paste(img, (x * each_size, y * each_size))
        x += 1
        if x == lines:
            x = 0
            y += 1
image = image.convert('RGB')
image.save("avatar2" + "/" + "all.jpg")
itchat.send_image("avatar2" + "/" + "all.jpg", "filehelper")
im = Image.open('avatar2/all.jpg')
im.show()
