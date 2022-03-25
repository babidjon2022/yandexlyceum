import sys
s = sys.stdin.read().split('\n')
shops = tuple(i.split('\t')[0] for i in s[1:])
books = s[0].split('\t')[1:]
d = list()
for i in s[1:]:
    lst = [int(j) for j in i.split('\t')[1:]]
    d.append(tuple(zip(books, lst)))
x = d.index(min(d, key=lambda y: sum(i[1] for i in y)))
print(shops[x])
for i in range(len(books)):
    print(f'{books[i]}\t{d[x][i][1]}')
