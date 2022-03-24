import pymorphy2
import sys
s = sys.stdin.read()


def delete_punctuation(s):
    new_str = ''
    for i in s:
        if i.isalpha():
            new_str += i
    return new_str


morph = pymorphy2.MorphAnalyzer()
print(len(tuple(filter(lambda x: morph.parse(x)[0].normal_form in {
      'видеть', 'увидеть', 'глядеть', 'примечать', 'узреть'},
    map(delete_punctuation, s.split())))))
