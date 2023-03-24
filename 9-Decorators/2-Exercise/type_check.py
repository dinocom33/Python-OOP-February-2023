def type_check(data_type):
    def decorator(func):
        def wrapper(*args):
            for arg in args:
                if isinstance(arg, data_type):
                    return func(*args)
                else:
                    return "Bad Type"

        return wrapper

    return decorator


@type_check(int)
def times2(num):
    return num * 2


print(times2(2))
print(times2('Not A Number'))
