import random


# TODO 生成200个验证码
# 验证码的生成规律：数字与大小写字母,长度为4
class Get_character_list:
    def __init__(self, choice: str):
        self.choice = choice

    def __str__(self):
        if self.choice == 1:
            return "获取了纯数字列表"
        elif self.choice == 2:
            return ("获得了小写字母的列表")
        elif self.choice == 3:
            return ("获得了大写字母的列表")
        elif self.choice == 4:
            return ("获得了所有字母（大小写）的列表")
        elif self.choice == "5":
            return "获得了所有字符（数字与字母的列表）"
        else:
            return "没有这项操作"

    def get_num(self):
        number_list = list()
        for i in range(10):
            number_list.append(str(i))
        return number_list

    def get_lowercase(self):
        capital_list = list()
        for i in range(26):
            capital_list.append(chr(97 + i))
        return capital_list

    def get_highercase(self):
        capital_list = list()
        for i in range(52):
            if i >= 26:
                capital_list.append(chr(65 + i - 26))
        return capital_list

    def get_words(self):
        capital_list = list()
        for i in range(52):
            if i < 26:
                capital_list.append(chr(97 + i))
            else:
                capital_list.append(chr(65 + i - 26))
        return capital_list

    def get_all_words(self):
        result1 = self.get_num()
        result2 = self.get_words()
        result1.extend(result2)
        return result1

    def output(self):
        if self.choice == "1":
            return self.get_num()
        elif self.choice == "2":
            return self.get_lowercase()
        elif self.choice == "3":
            return self.get_highercase()
        elif self.choice == "4":
            return self.get_words()
        elif self.choice == "5":
            return self.get_all_words()
        else:
            return []


if __name__ == '__main__':
    result_list = list()
    f = Get_character_list(choice="5")
    number_list = f.output()
    print(len(number_list))
    # 生成200个验证码
    for i in range(200):
        code_list = list()
        # 每个验证码长度为4
        for j in range(4):
            # 利用随机数字获得随机的字符
            index = random.randint(0, 61)
            # 将随机得到的字符储存起来
            code_list.append(number_list[index])
        # 将列表合成列表
        result_list.append("".join(code_list))
    print(result_list)
    # 检查所有验证码的长度是否为200
    print(len(result_list))

    # 将生成的验证码写入txt
    with open("./output/codes.txt", "w", encoding="UTF-8") as f:
        for i in result_list:
            f.write(i + "\n")
