s = [{''.join(sorted(list(i))): i} for i in (input().lower() for _ in range(int(input())))]
d = dict()
for i in s:
    a, b = tuple(i.items())[0]
    if a in d:
        d[a].append(b)
    else:
        d[a] = [b]
for i in d:
    d[i] = ' '.join(sorted(list(set(d[i]))))
print(*filter(lambda x: len(x.split()) > 1, sorted(d.values())), sep='\n')
