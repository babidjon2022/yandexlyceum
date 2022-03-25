def check_password(password):
    def decorator(func):
        def f(*args, **kwargs):
            if str(input('Введите пароль: ')) == password:
                return func(*args, **kwargs)
            print('Доступ запрещён')
            return None
        return f
    return decorator
