import pymorphy2
import sys
d = sys.stdin.read().split('\n')

morph = pymorphy2.MorphAnalyzer()
for i in d:
    word_morph = morph.parse(i)[0]
    animated = morph.parse('живой')[0]
    if 'NOUN' not in word_morph.tag:
        print('Не существительное')
        continue
    if word_morph.tag.animacy == 'anim':
        prefix = ''
    else:
        prefix = 'Не '
    if word_morph.tag.number == 'sing':
        print((prefix + animated.inflect({word_morph.tag.gender, 'nomn'}).word).capitalize())
    else:
        print((prefix + animated.inflect({'plur', 'nomn'}).word).capitalize())
