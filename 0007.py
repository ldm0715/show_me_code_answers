# TODO 统计目录中,代码行数。包括空行和注释，但是要分别列出来。

import os


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
    endswith = ["py"]
    endswith_tuple = tuple(endswith)
    return path.endswith(endswith_tuple)


def count_lines(files_list) -> (int, dict):
    print(f"共扫描到{len(files_list)}份Python代码文件")
    print("-" * 100)
    for file in files_list:
        f = open(file, "r", encoding="UTF-8")
        file_name = file.split("/")[-1]
        print(f"当前打开文件为:{file_name}")
        count_lines = get_count_lines(f)
        print(f"代码行数为:{count_lines}")
        f.close()
        f = open(file, "r", encoding="UTF-8")
        count_exegesis = get_exegesis_count(f)
        print(f"注释行数为:{count_exegesis}")
        f.close()
        f = open(file, "r", encoding="UTF-8")
        count_empty = get_empty_count(f)
        print(f"空行行数为:{count_empty}")
        f.close()
        print("-" * 100)


def get_count_lines(f):
    return len(f.readlines())


def get_exegesis_count(f):
    words = f.readlines()
    count = 0
    temp_list = list()
    for index in range(len(words)):
        words[index] = words[index].strip(" ")
        if len(words[index]) > 0:
            # print(words[index])
            if words[index][0] == "#":
                count += 1
                # print(words[index])

        if (words[index] == '"""\n') | (words[index] == '"""'):
            temp_list.append(index)
    # print(temp_list)
    for i in range(len(temp_list)):
        if i % 2 == 1:
            count += temp_list[i] - temp_list[i - 1] + 1

    return count


def get_empty_count(f):
    words = f.readlines()
    count = 0
    for word in words:
        if word == '\n':
            count += 1
    return count


if __name__ == '__main__':
    result = open_all_txt_file(r"/show_me_code/")
    # result = [r"D:/Python_Study/show_me_code/0004.py"]
    # print(result)
    count_lines(result)
