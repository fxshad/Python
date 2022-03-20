def check_int_dekor(func):
    """проверка типа аргумента"""
    def wrap(*args, **kwargs):
        if not isinstance(args[-1], int):
            print("переданный аргумент не является числом")
            res = None
        else:
            res = func(*args, **kwargs)
        return res
    return wrap


if __name__ == '__main__':
    pass

