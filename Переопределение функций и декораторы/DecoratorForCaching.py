def cached(func):
    cache = dict()

    def newfunc(*args, **kwargs):
        if (args, frozenset(kwargs.items())) not in cache:
            cache[(args, frozenset(kwargs.items()))] = func(*args, **kwargs)
            return func(*args, **kwargs)
        else:
            return cache[(args, frozenset(kwargs.items()))]
    return newfunc


if __name__ == '__main__':
    @cached
    def fib(n):
        return n * 100
    print(fib(5))
    print(fib(7))
    print(fib(5))
