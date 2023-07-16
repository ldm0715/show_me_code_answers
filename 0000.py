import cv2


# TODO 在头像上添加一个数字
image = cv2.imread("input/avatar.jpg")

# 画一个红色的圆
# thickness为负数时圆会被填充
cv2.circle(img=image, center=(590, 50), radius=50, color=(0, 0, 255), thickness=-1)
# 添加文本
cv2.putText(img=image, text="1", org=(570, 70), fontFace=cv2.FONT_HERSHEY_SIMPLEX,
            fontScale=2, color=(255, 255, 255), thickness=10)

# 保存处理后的图片
cv2.imwrite("./output/add_test1.png", image)
# 创建窗口，并设置自适应大小
cv2.namedWindow("add_test", cv2.WINDOW_AUTOSIZE)
# 展示图像
cv2.imshow("add_test", image)
# 设置手动停止
cv2.waitKey(0)

# from PIL import Image, ImageDraw, ImageFont
#
# background = Image.open("input/avatar.jpg")
# # 创建画笔对象
# draw = ImageDraw.Draw(background)
# # 绘制圆形
# draw.ellipse(((520, 0), (640, 120)), fill=(255, 255, 255), outline=(255, 255, 255), width=1)
# # 绘制文本
# font = ImageFont.truetype("simkai.ttf", size=100)
# draw.text((555, 15), text="1", fill="red", spacing=2, font=font)
# # 保存图片
# background.save("./output/add_test2.png")
# background.show()
