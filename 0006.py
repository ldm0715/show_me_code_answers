# TODO 5.统计出所有日记中最重要的内容

import os

# 生成大写字母合集
capital_list = list()
for i in range(52):
    if i < 26:
        capital_list.append(chr(97 + i))
    else:
        capital_list.append(chr(65 + i - 26))


def open_all_txt_file(input_path):
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
                files_list += open_all_txt_file(new_path)
            else:
                if is_txt(new_path):
                    files_list.append(new_path)
    else:
        print("该路径不存在，或者提取所有文件完成")
        return []
    return files_list


def is_txt(path: str) -> bool:
    return path.endswith(".txt")


def read_txt(path: str) -> (int, dict):
    """
    统计英文文本的个数
    :param test: 输入一个str
    :return: 统计英文文本
    """
    file_list = open_all_txt_file(path)
    print(file_list)
    import_word = dict()
    count = 1
    for file in file_list:
        word_dict = dict()
        f = open(file, "r", encoding="UTF-8")
        words = f.readlines()
        words = "".join(words)
        # print(words)
        # print(get_all_words(words))
        temp = get_all_words(words)

        for i in temp:
            if i not in word_dict.keys():
                word_dict[i] = 1
            else:
                word_dict[i] += 1
        word_dict = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)
        import_word[count] = word_dict[0]
        count += 1
    return len(file_list), import_word


def get_all_words(test: str):
    """
    统计英文文本的个数
    :param test: 输入一个str
    :return: 统计英文文本
    """
    for i in test:
        if i not in capital_list:
            test = test.replace(i, " ")
    # print(test)
    result = test.split(" ")
    # 将数据复制一份
    temp = result.copy()
    # 打印初始数据
    # print(result)

    for word in result:
        if len(word) <= 0:
            temp.remove(word)
    return temp
    # print("英文文本中单词的个数：%d" % len(result))


if __name__ == '__main__':
    input_path = "F:/txt_test"
    num, result = read_txt(input_path)
    print("-" * 100)
    print(f"共扫描到{num}篇日记")
    for i in range(1, num + 1):
        print(f"第{i}篇日记中出现最多的词为 \"{result[i][0]}\",在日记中出现了{result[i][1]}次")

# path = "./THUMBS.png"
#
# endswith = ["png", "jpg"]
# endswith_tuple = tuple(endswith)
#
# bool_endswith = path.endswith(endswith_tuple)
# print(bool_endswith)
