import pymorphy2
import sys
s = sys.stdin.read()
morph = pymorphy2.MorphAnalyzer()
d = dict()


def clear_punctuation(s):
    newstr = ''
    for i in s:
        if i.isalpha():
            newstr += i
    return newstr


for i in s.split():
    if not clear_punctuation(i):
        continue
    i = clear_punctuation(i)
    word_morph = morph.parse(i)[0]
    if word_morph.score <= 0.5 or word_morph.tag.POS != 'NOUN':
        continue
    if word_morph.normal_form not in d:
        d[word_morph.normal_form] = 1
    else:
        d[word_morph.normal_form] += 1

print(*tuple(
    map(lambda x: x[0],
        sorted(d.items(), key=lambda x: (x[1], x[0]), reverse=True)))[:10])
