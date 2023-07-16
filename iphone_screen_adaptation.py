# TODO 将所有图片转化成不大于iphone5（1136*640 ）的显示大小
import os
from PIL import Image


class Adaptation_iphone:
    def __init__(self, input_path: str, output_path: str, phone_model: str):
        self.input_path = input_path
        self.output_path = output_path
        self.phone_model = phone_model

    def open_all_imag_file(self, input_path):
        """
        打开所有文件
        :param input_path: 输入路径
        :return: 存有所有文件路径的list
        """
        print(f"当前打开路径为：{input_path}")
        files_list = list()
        if os.path.exists(input_path):
            files = os.listdir(input_path)
            for file in files:
                new_path = input_path + "/" + file
                if os.path.isdir(new_path):
                    files_list += self.open_all_imag_file(new_path)
                else:
                    if self.is_image(new_path):
                        files_list.append(new_path)
        else:
            print("该路径不存在，或者提取所有文件完成")
            return []
        return files_list

    def is_image(self, path):
        """
        判断是否为图片
        :param path: 文件路径
        :return: bool
        """
        endswith = ["png", "jpg", "bmp"]
        endswith_tuple = tuple(endswith)

        return path.endswith(endswith_tuple)

    def judgement_image(self, imag):
        """
        得到缩放范围
        :param imag:输入图片
        :return:缩放倍数
        """
        screen_width, screen_height = self.screen_resolution()

        scale = 1
        if imag.height > imag.width:
            scale = screen_height / imag.height
            while imag.width * scale > screen_width:
                scale -= 0.1

        if imag.width > imag.height:
            scale = screen_width / imag.width
            while imag.height * scale > screen_height:
                scale -= 0.1
        return scale

    def resize_imag(self):
        """
        重置图片的分辨率
        :param input_path:输入图片路径
        :param output_path:输出图片路径
        :return:None
        """
        file_list = self.open_all_imag_file(self.input_path)
        print("---所有文件提取完成!---")
        num = 0

        for path in file_list:
            imag = Image.open(path)
            scale = self.judgement_image(imag)
            # print(f"scale={scale}")
            height = int(imag.height * scale)
            weight = int(imag.width * scale)
            print(f"height={height},weight={weight}")
            type = imag.format
            result = imag.resize((weight, height), Image.Resampling.LANCZOS)
            # Image.Resampling.NEAREST ：低质量
            # Image.Resampling.BILINEAR：双线性
            # Image.Resampling.BICUBIC ：三次样条插值
            # Image.Resampling.LANCZOS：高质量
            result.save(self.output_path + f"{num}.png", type)
            num += 1
        print(f"当前适配机型: iphone {self.phone_model} \n共处理{num}张图片,输出文件夹为：{self.output_path}")

    def screen_resolution(self):
        if self.phone_model == "5":
            screen_width = 640
            screen_height = 1136
            return screen_width, screen_height
        elif (self.phone_model == "6") | (self.phone_model == "6s"):
            screen_width = 750
            screen_height = 1334
            return screen_width, screen_height
        else:
            print("未适配当前机型，目前仅支持\"iPhone 5 ,6 ,6s\"")
            exit(0)

    def run(self):
        self.resize_imag()


if __name__ == '__main__':
    input_path = r"F:/image_test"
    output_path = "/output/"
    i = Adaptation_iphone(input_path, output_path, "5")
    i.run()
