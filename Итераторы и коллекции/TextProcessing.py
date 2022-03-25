from itertools import chain
from sys import stdin
phrases = [''.join(j for j in i if j.isalpha()) for i in list(
    chain(i for j in stdin.read().split('\n') for i in j.split()))]
capitals = list(
    filter(lambda x: x == x.capitalize(), phrases))
used_words = set()
capitals1 = capitals.copy()
for i in range(len(capitals1)):
    if capitals1[i][1] not in used_words:
        used_words.add(capitals1[i][1])
    else:
        capitals.remove(capitals1[i])
capitals = {i[1]: i[0] for i in capitals}
capitals_sorted = sorted(capitals.keys())
capitals = {i: capitals[i] for i in capitals_sorted}
print(*map(lambda x: f'{capitals[x]} - {x}', (i for i in capitals)), sep='\n')
