# Пароль - 12345
def check_password(func):
    def newf(*args, **kwargs):
        if str(input('Введите пароль: ')) == '12345':
            return func(*args, **kwargs)
        else:
            print('В доступе отказано')
            return None

    return newf


@check_password
def fibonacci(n):
    lst = [0, 1]
    for _ in range(n - 2):
        n = lst[-1] + lst[-2]
        lst.append(n)
    return lst
