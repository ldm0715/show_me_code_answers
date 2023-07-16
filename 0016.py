# TODO 将numbers.txt纯文本文件写入numbers.xls中

import json
import xlwt

f = open("./input/numbers.txt", "r", encoding="UTF-8")
data = f.read()
json_data = json.loads(data)
print(json_data)

book = xlwt.Workbook(encoding="UTF-8")

sheet = book.add_sheet("numbers", cell_overwrite_ok=True)

style = xlwt.XFStyle()

font = xlwt.Font()
font.name = "Times New Roman"
font.bold = True

alignment = xlwt.Alignment()

# 水平居中 May be: HORZ_GENERAL, HORZ_LEFT, HORZ_CENTER, HORZ_RIGHT, HORZ_FILLED, HORZ_JUSTIFIED, HORZ_CENTER_ACROSS_SEL, HORZ_DISTRIBUTED
alignment.horz = xlwt.Alignment.HORZ_RIGHT

# 我上下对齐 May be: VERT_TOP, VERT_CENTER, VERT_BOTTOM, VERT_JUSTIFIED, VERT_DISTRIBUTED
alignment.vert = xlwt.Alignment.VERT_CENTER

for x in range(len(json_data)):
    for y in range(len(json_data[0])):
        sheet.write(x, y, json_data[x][y], style)

book.save("./output/numbers.xls")
