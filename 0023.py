"""
用python操作mysql完成一个在线留言板
    1.设计在线留言板表
    2.通过python语言实现
"""
import pymysql
from flask import Flask, render_template, request
import time

app = Flask(__name__)


# 连接数据库并发起请求 获取请求结果
def model(sql):
    # 1.链接mysql数据库
    db = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        password='1234',
        # 打开自动提交
        autocommit=True,
        database='db1',
        cursorclass=pymysql.cursors.DictCursor
    )
    try:
        # 2.创建游标对象
        cursor = db.cursor()
        # 3.执行sql语句
        res = cursor.execute(sql)
        # 在执行sql语句时，注意进行提交
        db.commit()
        # 4.提取结果
        data = cursor.fetchall()
        if data:
            return data
        else:
            return res
    except:
        # 当代码出现错误时，进行回滚
        db.rollback()
    finally:
        # 6.关闭数据库连接
        db.close()


# 留言板列表 显示留言信息
@app.route("/")
def hello():
    # 1.获取所有的留言板数据
    # 2.把数据分配到模板中(html页面)
    row = model("select * from test1")
    return render_template('index.html', data=row)


# 定义视图 显示留言添加的页面
@app.route('/add')
def add():
    return render_template('add.html')


# 定义视图函数 接收表单数据，完成数据的入库
@app.route('/insert', methods=['POST'])
def insert():
    # 1.接收表单数据
    data = request.form.to_dict()
    data['date'] = time.strftime('%Y-%m-%d %H:%M:%S')
    print(data)
    # 2.把数据添加到数据库
    sql = f'insert into lyb values(null,"{data["nikename"]}","{data["info"]}","{data["date"]}")'
    res = model(sql)
    print(res)
    # 3.成功后页面跳转到 留言列表界面
    if res:
        return '<script>alert("留言成功！");location.href="/"</script>'
    else:
        return '<script>alert("留言发布失败！");location.href="/add"</script>'


# 删除 一行留言
@app.route("/delete")
def delete():
    id = request.args.get('id')
    sql = f'delete from lyb where id={id}'
    res = model(sql)
    if res:
        return '<script>alert("删除成功！");location.href="/"</script>'
    else:
        return '<script>alert("删除失败！");location.href="/"</script>'


# 修改留言视图界面  不能修改id 即使在text文本框中修改了也没用
@app.route("/update")
def update():
    id = request.args.get('id')
    sql = f'select * from lyb where id={id}'
    res = model(sql)
    return render_template('update.html', data=res)


# 修改留言视图函数 在数据库中修改留言内容
@app.route('/modify', methods=['POST'])
def modify():
    # 1.接收表单数据
    data = request.form.to_dict()
    data['date'] = time.strftime('%Y-%m-%d %H:%M:%S')
    # 2.把数据添加到数据库
    sql = f'update lyb set nikename="{data["nikename"]}",info="{data["info"]}",date="{data["date"]}" where id={int(data["id"])}'
    res = model(sql)
    # 3.成功后页面跳转到 留言列表界面
    if res:
        return '<script>alert("修改成功！");location.href="/"</script>'
    else:
        return '<script>alert("留言修改失败！");location.href="/"</script>'


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')
