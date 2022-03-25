def linear(lst):
    if lst == list():
        return list()
    if isinstance(lst, list):
        return linear(lst[0]) + linear(lst[1:])
    return [lst]
