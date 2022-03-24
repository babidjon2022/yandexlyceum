import pymorphy2

s = input().lower()
morph = pymorphy2.MorphAnalyzer()
dct = {
    0: ('nomn', 'Именительный падеж'),
    1: ('gent', 'Родительный падеж'),
    2: ('datv', 'Дательный падеж'),
    3: ('accs', 'Винительный падеж'),
    4: ('ablt', 'Творительный падеж'),
    5: ('loct', 'Предложный падеж')
}


def print_cases(s, n):
    if n == 0:
        n = 'sing'
        print('Единственное число:')
    else:
        n = 'plur'
        print('Множественное число:')
    for i in range(6):
        print(f'{dct[i][1]}: {morph.parse(s)[0].inflect({dct[i][0], n}).word}',
              sep='\n')


if len(s.split()) == 1 and 'NOUN' in morph.parse(s)[0].tag:
    for i in range(2):
        print_cases(s, i)
else:
    print('Не существительное')
