import xlsxwriter
import sys

data = [i.split() for i in sys.stdin.read().split('\n')]
workbook = xlsxwriter.Workbook('res.xlsx')
worksheet = workbook.add_worksheet()
for row, (item, price) in enumerate(data):
    worksheet.write(row, 0, item)
    worksheet.write(row, 1, int(price))
chart = workbook.add_chart({'type': 'pie'})
print(len(data))
chart.add_series({
    'categories': f'=Sheet1!$A$1:$A{len(data)}',
    'values': f'=Sheet1!$B$1:$B{len(data)}'
})
worksheet.insert_chart('C3', chart)
workbook.close()
