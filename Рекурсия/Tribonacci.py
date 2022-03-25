lst = [0, 0, 1]


def tribonacci(n):
    if n < 3:
        return lst[n]
    if n > 3:
        lst.append(lst[-3] + lst[-2] + lst[-1])
        return tribonacci(n - 1)
    return lst[-1]
