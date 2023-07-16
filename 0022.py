# TODO 使用05.py实现对iPhone 6、iPhone 6 Plus分辨率的适配

# 自己写的适配iphone屏幕的类
from iphone_screen_adaptation import Adaptation_iphone

input_path = r"F:/image_test"
output_path1 = "../show_me_code/output/iphone6/"
output_path2 = "../show_me_code/output/iphone6s/"

phone1 = Adaptation_iphone(input_path, output_path1, "6")
phone2 = Adaptation_iphone(input_path, output_path2, "6s")

phone1.run()
phone2.run()
