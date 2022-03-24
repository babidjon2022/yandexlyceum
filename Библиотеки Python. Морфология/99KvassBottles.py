import pymorphy2

morph = pymorphy2.MorphAnalyzer()

for i in range(99, 0, -1):
    print(
        f'В холодильнике {i} {morph.parse("бутылка")[0].make_agree_with_number(i).word} кваса.'
    )
    print('Возьмём одну и выпьем.')
    if (i - 1) % 10 == 1 and (i - 1) != 11:
        print(
            f'Осталась {i - 1}',
            f'{morph.parse("бутылка")[0].make_agree_with_number(i - 1).word} кваса.'
        )
    else:
        print(
            f'Осталось {i - 1}',
            f'{morph.parse("бутылка")[0].make_agree_with_number(i - 1).word} кваса.'
        )
