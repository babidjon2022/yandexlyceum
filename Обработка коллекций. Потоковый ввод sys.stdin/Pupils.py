d = list()
for i in range(int(input())):
    d.append(list())
    for j in range(int(input())):
        s = input().split()
        d[-1].append((s[0], int(s[1])))
d = list(map(lambda i: any(map(lambda x: x[1] == 5, i)), d))
print('ДА') if all(d) else print('НЕТ')
