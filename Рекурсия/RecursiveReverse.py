def recursive_reverse(lst):
    if not lst:
        return list()
    else:
        return recursive_reverse(lst[1:]) + [lst[0]]
