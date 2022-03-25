def use_uppercased_arguments(old_func):
    def new_func(*args, **kwargs):
        args_upcased = [str(arg).upper() for arg in args]
        old_func(*args_upcased, **kwargs)

    return new_func


print = use_uppercased_arguments(print)
