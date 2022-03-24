import pymorphy2

morph = pymorphy2.MorphAnalyzer()

word_morph = morph.parse(input())[0]
if 'VERB' not in word_morph.tag and 'INFN' not in word_morph.tag:
    print('Не глагол')
else:
    print('Прошедшее время:')
    for i in ('masc', 'femn', 'neut'):
        print(word_morph.inflect({'sing', i}).word)
    print(word_morph.inflect({'plur'}).word)
    print('Настоящее время:')
    for i in ('1per', '2per', '3per'):
        for j in ('sing', 'plur'):
            print(word_morph.inflect({i, j}).word)
