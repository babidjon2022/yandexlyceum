def recursive_len(lst):
    if not lst:
        return 0
    return 1 + recursive_len(lst[1:])