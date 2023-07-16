# TODO 当用户输入敏感词语，则用 星号 * 替换


def get_result(filtered_words: list, usr_input: str) -> str:
    for filtered_word in filtered_words:
        if filtered_word in usr_input:
            print(f"触发的违禁词：{filtered_word}")
            n = len(filtered_word)
            usr_input = usr_input.replace(filtered_word, "*" * n)
    return usr_input


if __name__ == '__main__':
    # 获取敏感词列表
    f = open("./input/filtered_words.txt", "r", encoding="UTF-8")
    temp_list = f.readlines()
    filtered_words = list()
    for filtered_word in temp_list:
        word = filtered_word.strip()
        filtered_words.append(word)
    print(filtered_words)

    usr_input = input("请输入内容：")

    result = get_result(filtered_words=filtered_words, usr_input=usr_input)
    print(result)
