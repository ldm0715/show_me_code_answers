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