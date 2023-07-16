# TODO 将数据写入MySQL
from pymysql import Connection

# 创建连接
conn = Connection(
    host='localhost',
    port=3306,
    user='root',
    password='1234',
    # 打开自动提交
    autocommit=True
)
# 打印数据库对象
print(conn.get_server_info())
# 选择数据库
conn.select_db("db1")
# 创建一个游标对象
cursor = conn.cursor()
# 创建表
# cursor.execute("create database test")

data_list = list()
# 打开文件将数据读出
with open("./output/codes.txt", "r", encoding="UTF-8") as f:
    words = f.readlines()
    for word in words:
        word = word.strip()
        # print(word)
        data_list.append(word)
print(list)
# 执行sql操作
index = 0
for record in list:
    sql = f"insert into test values ('{index}','{record}')"
    index += 1
    cursor.execute(sql)
# 关闭连接
cursor.close()
