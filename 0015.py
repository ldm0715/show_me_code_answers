# TODO 将纯文本文件 city.txt中的城市信息写入city.xls 文件中

import json
import xlwt

# 打开文件并读取文件
f = open("./input/city.txt", "r", encoding="UTF-8")
data = f.read()
json_data = json.loads(data)
print(json_data)

# 创建一个列表
book = xlwt.Workbook(encoding="UTF-8")
# 创建一个sheet
sheet = book.add_sheet("city", cell_overwrite_ok=True)

# 创建样式
style1 = xlwt.XFStyle()
style2 = xlwt.XFStyle()

# 设置字体样式
font1 = xlwt.Font()
font1.name = '宋体'

font2 = xlwt.Font()
font2.name = 'Times New Roman'

# 创建对其格式的对象 Create Alignment
alignment = xlwt.Alignment()

# 水平居中 May be: HORZ_GENERAL, HORZ_LEFT, HORZ_CENTER, HORZ_RIGHT, HORZ_FILLED, HORZ_JUSTIFIED, HORZ_CENTER_ACROSS_SEL, HORZ_DISTRIBUTED
alignment.horz = xlwt.Alignment.HORZ_LEFT

# 我上下对齐 May be: VERT_TOP, VERT_CENTER, VERT_BOTTOM, VERT_JUSTIFIED, VERT_DISTRIBUTED
alignment.vert = xlwt.Alignment.VERT_CENTER

style1.font = font1
style1.alignment = alignment

style2.font = font2
style2.alignment = alignment

# 写入表头
cols = ["序号", "城市名称"]
for i in range(len(cols)):
    sheet.write(0, i, cols[i], style1)

# 写入数据
for x in range(1, len(json_data) + 1):
    for y in range(1, len(json_data["1"])):
        sheet.write(x, y, json_data[str(x)], style1)
    # 写入第一列的序号
    sheet.write(x, 0, x, style2)

# 保存表格
book.save("./output/city.xls")
