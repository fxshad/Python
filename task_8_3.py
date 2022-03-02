from functools import wraps


def type_logger(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        markup = func(*args, **kwargs)
        for i in args:
            print(f"{func.__name__}  ({i}:{type(i)})", end=",   ")
        for i in kwargs:
            print(f"{func.__name__} ({i}:{type(i)})", end=",   ")
        print(f"type result({type(markup)})")

        return markup
    return wrap


@type_logger
def calc_cube(x):
    return x ** 3.9

print("\nEnd")


