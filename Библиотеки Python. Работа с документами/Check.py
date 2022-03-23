import xlsxwriter


def export_check(text):
    workbook = xlsxwriter.Workbook('res.xlsx')
    worksheet = workbook.add_worksheet()
    text = tuple(map(lambda x: x.split('\t'), text.splitlines()))
    for i in range(len(text)):
        worksheet.write(i, 0, text[i][0])
        worksheet.write(i, 1, text[i][1])
        worksheet.write(i, 2, text[i][2])
        worksheet.write(i, 3, f'=B{i + 1}*C{i + 1}')
    worksheet.write(len(text), 0, 'Итого')
    worksheet.write(len(text), 3, f'=SUM(D1:D{len(text)})')
    workbook.close()
