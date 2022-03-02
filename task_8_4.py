def check_num(x):
    if type(x) == float or type(x) == int:
        pass
    else:
        raise TypeError("Не число")
    if x <= 0:
        raise ValueError("Неверное число")


def check_decor(checker):## пишите реализацию декоратора здесь
    def val_checker(func):
        def wrap(*args):
            checker(*args)
            markup = func(*args)
            return markup
        return wrap
    return val_checker


@check_decor(check_num)  # не забудьте про аргумент-функцию
def calc_cube(x):
    """Возведение числа в третью степень"""
    return x ** 3


if __name__ == '__main__':
    print(calc_cube(5))
    print(calc_cube('ss'))

print("\nEnd")
