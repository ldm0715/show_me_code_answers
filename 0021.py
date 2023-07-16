# TODO 使用哈希加盐算法加密用户密码，模拟用户登陆与注册的场景

import os
import hashlib
from pymysql import Connection
from base64 import b64encode, b64decode

# 密码加密步骤
"""
1. 使用CSPRNG生成一个长度足够的盐值，盐值最好和字节数（bytes）相等
2. 将盐值混入密码，并使用标准的加密哈希函数进行加密，如SHA256(Python中直接调用hashlib包)
3. 把哈希值和盐值一起存入数据库中对应此用户的那条记录
"""

# 密码生成步骤
"""
1. 从数据库取出用户的密码哈希值和对应盐值
2. 将盐值混入用户输入的密码，并且使用同样的哈希函数进行加密
3. 比较上一步的结果和数据库储存的哈希值是否相同，如果相同那么密码正确，反之密码错误
"""

# 生成盐值
salt = os.urandom(32)
# print(f"生成的盐值：{salt}")

# 哈希加密，这里选择md5
# hexdigest是转化为16进制
hash_1 = hashlib.md5("hello".encode('utf-8')).hexdigest()
# print(f"字节数：{len(hash_1.encode('utf-8'))}")


# 创建数据库连接
conn = Connection(
    host='localhost',
    port=3306,
    user='root',
    password='1234',
    # 打开自动提交
    autocommit=True
)

# 打印数据库信息
print(f"当前服务器使用：MySQL {conn.get_server_info()}")

# 选择数据库
conn.select_db("db1")

# 用来存储从数据库读出的所有数据
usr_dict = dict()


# 读取数据库的所有信息
def get_data_from_mysql():
    global usr_dict
    # 创建一个游标对象
    cursor = conn.cursor()

    # 需要写入excel表数据
    sql = 'select * from %s;' % ("hash_test")
    # 读取数据
    cursor.execute(sql)
    # 读取表结构定义(表头)
    fileds = [filed[0] for filed in cursor.description]
    # print(fileds)
    # 所有数据
    all_date = cursor.fetchall()
    # print(all_date[0][0])

    for j in range(len(all_date)):
        usr_dict[all_date[j][0]] = {fileds[1]: all_date[j][1], fileds[2]: b64decode(all_date[j][2])}
    # print(f"当前所有数据：{usr_dict}")


# 设置一个超级账户
# usr_dict = {'ldm123': {'hash': "267798f30e91c5174bdd550fbc015ad4",
#                        'salt': b't\xbd+P,\x8c*\xd7\x1e[b\xc5o\x99\x1f\xe9? \x10;Kh/\x9dg\xc3SMMTS\xe7'}}


def usr_register():
    """
    用户注册
    :return: None
    """
    global usr_dict

    while True:
        usr_name = input("请输入用户名：")

        if usr_name in usr_dict.keys():
            print("当前用户已存在，请重新输入")
        else:
            password = input("请输入 密码：")
            hash, salt = encode_password(password=password)
            sql = f"insert into hash_test values ('{usr_name}','{hash}','{salt}')"
            # 创建一个游标对象
            cursor = conn.cursor()
            # 执行写入
            cursor.execute(sql)
            usr_dict[usr_name] = dict(hash=hash, salt=salt)
            print("用户注册成功！")
            # print(f"当前用户信息：{usr_dict[usr_name]}")
            get_data_from_mysql()
            break


def encode_password(password):
    """
    对密码进行加密
    :param password: 用户密码
    :return: 机密后的hash值，salt
    """
    # print(f"用户名：{usr_name}  密码：{password}")
    hash_password = hashlib.md5(password.encode("utf-8")).hexdigest()
    # print(f"MD5加密：{hash_password}")
    salt_num = len(hash_password.encode('utf-8'))
    # print(f"当前字节数：{salt_num}")
    salt = os.urandom(salt_num)
    # print(f"生成{salt_num}位的盐值：{salt}")
    salt_and_hash = hashlib.md5(password.encode('UTF-8') + salt).hexdigest()
    # 对hash值进行加密，以便存入数据库中
    salt = b64encode(salt).decode('utf-8')
    # print(f"加入盐值后的MD5加密：{salt_and_hash}")
    # usr_dict[usr_name] = dict(hash=salt_and_hash, salt=salt)
    # print(usr_dict)
    return salt_and_hash, salt


def Verify_the_password(usr_name, password):
    """
    校验hash值是否一致
    :param usr_name: 用户名
    :param password: 用户密码
    :return: 判断结果（bool）
    """
    global usr_dict
    hash = usr_dict[usr_name]['hash']
    salt = usr_dict[usr_name]['salt']
    hash_password = hashlib.md5((password.encode('utf-8') + salt)).hexdigest()
    if hash_password == hash:
        return True
    return False


def usr_login():
    """
    用户登陆
    :return: None
    """
    get_data_from_mysql()
    global usr_dict
    while True:
        usr_name = input("请输入用户名：")

        if usr_name not in usr_dict.keys():
            print("当前用户未注册")
            break
        else:
            password = input("请输入 密码：")
            if Verify_the_password(usr_name=usr_name, password=password):
                print(f"{usr_name}你好，欢迎登陆!")
                break
            else:
                print("用户名或密码错误，请重新输入")


def menu():
    """
    菜单系统
    :return: 返回用户的选择（str）
    """
    print(" ----欢迎使用本系统----")
    print(" ____________________")
    print("|\t\t1.注册\t\t |")
    print("|\t\t2.登陆\t\t |")
    print("|\t\t3.退出\t\t |")
    print("￣￣￣￣￣￣￣￣￣￣￣￣")
    choose = input("请输入您的选择：")
    return choose


if __name__ == '__main__':
    while True:
        choose = menu()
        if choose == "1":
            usr_register()
            print("-" * 100)
        elif choose == "2":
            usr_login()
            print("-" * 100)
        elif choose == "3":
            print("感谢您的使用！")
            conn.close()
            exit(0)
        else:
            print("没有这个选项，请重新输入")
            print("-" * 100)
