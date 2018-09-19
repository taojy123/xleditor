# xleditor
打开并在原有基础上编辑 xls / xlsx 文档

[![PyPI Downloads](https://pypistats.com/badge/xleditor.png)](https://pypistats.com/package/xleditor)


Useage:

```
# pip install xlrd
# pip install xlutils

import xleditor

book = xleditor.open_workbook('old.xls')
sheet = book.get_sheet_by_index(0)

print sheet.get_value(3, 0)
sheet.write(0, 5, 'hello world')

book.save('new.xls')

```