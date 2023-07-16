# TODO 找到一个网页的正文部分

# 打开html
wy = open("./input/小米官网图片.html", "r", encoding="UTF-8")

# 获取html文件内容
words = wy.readlines()
html_list = list()
for word in words:
    # 去除空格
    temp = word.strip(" ")
    html_list.append(temp)
print(html_list)

body = list()
for index in range(len(html_list)):
    num = index
    if html_list[index].strip(" ") == "<body>\n":
        num += 1
        while html_list[num].strip(" ") != "</body>\n":
            if html_list[num].strip(" ") != "\n":
                body.append(html_list[num].strip("\n"))
            num += 1
print("-" * 100)
print("网页的正文部分为：")
for i in body:
    print(i)
