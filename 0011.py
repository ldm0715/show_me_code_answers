# TODO 敏感词文本文件 filtered_words.txt，里面的内容为以下内容，
#  当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。


def get_result(filtered_words: list, usr_input: str) -> str:
    for filtered_word in filtered_words:
        if filtered_word in usr_input:
            return "Freedom"
    return "Human Rights"


if __name__ == '__main__':
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
