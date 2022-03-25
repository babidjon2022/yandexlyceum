def rec_linear_sum(lst):
    if not lst:
        return 0
    else:
        return rec_linear_sum(lst[1:]) + lst[0]
