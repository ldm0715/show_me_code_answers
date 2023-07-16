# TODO 将纯文本文件 student.txt（学生信息）写到 student.xls 文件中

import json
import xlwt
import pandas as pd

book = xlwt.Workbook(encoding='utf-8', style_compression=0)

# 创建一个sheet
sheet = book.add_sheet('students', cell_overwrite_ok=True)

# 打开文件
f = open("./input/students.txt", "r", encoding="UTF-8")
data = f.read()
json_temp: dict = json.loads(data)
print(json_temp)
print(len(json_temp['1']))

# 设置写入样式
# 初始化样式
style1 = xlwt.XFStyle()
style2 = xlwt.XFStyle()

# 创建字体
font1 = xlwt.Font()
font2 = xlwt.Font()

# 选择字体
font1.name = 'Times New Roman'
font1.bold = False
font2.name = '宋体'
font2.bold = False

# 设置单元格宽度
sheet.col(0).width = 1500

# 创建对其格式的对象 Create Alignment
alignment = xlwt.Alignment()

# 水平居中 May be: HORZ_GENERAL, HORZ_LEFT, HORZ_CENTER, HORZ_RIGHT, HORZ_FILLED, HORZ_JUSTIFIED, HORZ_CENTER_ACROSS_SEL, HORZ_DISTRIBUTED
alignment.horz = xlwt.Alignment.HORZ_CENTER

# 我上下对齐 May be: VERT_TOP, VERT_CENTER, VERT_BOTTOM, VERT_JUSTIFIED, VERT_DISTRIBUTED
alignment.vert = xlwt.Alignment.VERT_CENTER

# 设置字体
style1.font = font1
style1.alignment = alignment
style2.font = font2
style2.alignment = alignment

# 创建列名
loc = ["序号", "姓名", "score1", "score2", "score3"]

# 写入表头
for i in range(0, len(loc)):
    sheet.write(0, i, loc[i], style2)

# 写入表格
for i in range(len(json_temp)):
    for j in range(len(json_temp['1'])):
        sheet.write(i + 1, j + 1, json_temp[str(i + 1)][j], style1)
    sheet.write(i + 1, 0, i + 1)

book.save("./output/students.xls")
