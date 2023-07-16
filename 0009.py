# TODO 找到一个网页的所有链接

# 打开html
wy = open("./input/小米官网图片.html", "r", encoding="UTF-8")

# 获取html文件内容
words = wy.readlines()
html_list = list()
for word in words:
    # 去除空格
    temp = word.strip(" ")
    html_list.append(temp)
# print(html_list)

links_dict = dict()
for html in html_list:
    html = html.strip(" ")
    if "<a" in html:
        link = html.split('"')[1]
        # print(html)
        link_name = html.lstrip("<a").rstrip("</a>\n").split(">")[1]
        links_dict[link_name] = link

print(links_dict)

print(f"该网页中有{len(links_dict)}个链接：")
i = 1
for name in links_dict.keys():
    print(f"No.{i} \t{name}:{links_dict[name]}")
    i += 1




