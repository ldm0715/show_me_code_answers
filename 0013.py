# TODO 写一个爬虫程序爬取图片（贴吧就算了，爬自己的博客吧）

import requests
import urllib
from bs4 import BeautifulSoup
from tqdm import tqdm

reponse = requests.get("")
data = reponse.content.decode()
soup = BeautifulSoup(data, 'lxml')

all_img = soup.find_all("img")
# print(all_img)

num = 0
for i in tqdm(all_img, "下载图片："):
    src_ = i["src"]
    if src_[:8] != "/themes/":
        num += 1
        urllib.request.urlretrieve(src_, "./output/images/%s.jpg" % (num))
    elif src_[:8] == "/themes/":
        src_ = "https://www.gcnanmu3125.xyz" + src_
        num += 1
        urllib.request.urlretrieve(src_, "./output/images/%s.jpg" % (num))

print(f"共从网页中爬取到{num}张图片，图片存放路径为：\"./output/images/\"")
