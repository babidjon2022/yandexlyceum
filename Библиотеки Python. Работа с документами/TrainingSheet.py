import docxtpl


def create_training_sheet(class_name, subject_name, tpl_name, *tuples):
    template = docxtpl.DocxTemplate(tpl_name)
    marks = list()
    tuples = sorted(tuples, key=lambda x: x[0])
    for i in range(len(tuples)):
        num, fio, mark = i, *tuples[i]
        marks.append({'num': num + 1, 'fio': fio, 'mark': mark})
    parameters = {
        'class_name': class_name,
        'subject_name': subject_name,
        'marks': marks
    }
    template.render(parameters)
    template.save('res.docx')


if __name__ == '__main__':
    create_training_sheet("3И", "Математика", "tpl.docx", ("Петров Петр", "5"),
                          ("Иванов Иван", "5"), ("Сергеев Сергей", "3"),
                          ("Никитин Никита", "4"))
