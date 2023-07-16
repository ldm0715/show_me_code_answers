# TODO 统计英文文本中单词的个数

# 生成大写字母合集
capital_list = list()
for i in range(52):
    if i < 26:
        capital_list.append(chr(97 + i))
    else:
        capital_list.append(chr(65 + i - 26))


# print(capital_list)

def count_words(test: str):
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
    print(temp)
    # print("英文文本中单词的个数：%d" % len(result))
    return len(temp)


if __name__ == '__main__':
    # 18单词
    test1 = "I believe in the power of the mind, " \
            "mind you're at the height of the final decision"

    # 27单词
    test2 = "As long as we believe that the strength of mind, " \
            "changes our attitude and courage to face several disappointments in life, " \
            "do not despair, brave go on."

    # 45词
    test3 = "I believe in the power of the mind, " \
            "mind you're at the height of the final decision." \
            "As long as we believe that the strength of mind, " \
            "changes our attitude and courage to face several disappointments in life, " \
            "do not despair, brave go on."
    # 16词
    test4 = "我 believe in the power of the mind, " \
            "mind you're at the height of the 最后 decision"


    result1 = count_words(test1)
    result2 = count_words(test2)
    result3 = count_words(test3)
    result4 = count_words(test4)

    print("该英文文本中单词的个数：%d" % result1)
    print("该英文文本中单词的个数：%d" % result2)
    print("该英文文本中单词的个数：%d" % result3)
    print("该英文文本中单词的个数：%d" % result4)
