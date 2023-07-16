# TODO 使用 Python 生成类似于下图中的字母验证码图片
from PIL import Image, ImageFont, ImageDraw
import random
import string
# 自己写的生成一个字符的类
from get_character_list import Get_character_list

# 获得一个四位验证码
result_str = ""
character_list = string.ascii_letters + string.digits
print(character_list)
for i in range(4):
    index = random.randint(0, 61)
    word = character_list[index]
    result_str += word
print(f"生成的随机验证码：{result_str}")


# 随机颜色
def get_random_color():
    return (random.randint(0, 150), random.randint(0, 150), random.randint(0, 150))


# 随机位置
def get_random_loc(width, height):
    x = random.randint(0, width - 1)
    y = random.randint(0, height - 1)
    return x, y


# 绘制背景
background = Image.new(mode="RGB", size=(300, 80), color="white")

# 设定字体
font = ImageFont.truetype("simkai.ttf", size=60)

# 画笔对象
draw = ImageDraw.Draw(background)

# 绘制字符
start_x = background.width / 6
start_y = background.height / 6
for i in range(4):
    draw.text(xy=(start_x, start_y), text=result_str[i], font=font, fill=get_random_color())
    start_x += 60

# 绘制线条
for i in range(4):
    x1, y1 = get_random_loc(background.width, background.height)
    x2, y2 = get_random_loc(background.width, background.height)
    while (x1 == x2) & (y1 == y2):
        x2, y2 = get_random_loc(background.width, background.height)
    draw.line(xy=[(x1, y1), (x2, y2)], fill=get_random_color())

# 绘制点
for i in range(2000):
    x, y = get_random_loc(background.width, background.height)
    draw.point(xy=(x, y), fill=get_random_color())

# 展示图片
background.show()
# 保存图片
save_path = "./output/code.png"
background.save(save_path, format="png")
print(f"图片保存路径为：{save_path}")
