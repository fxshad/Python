class CustomErrorClass(Exception):
    pass
    # def __str__(self):
    #     return f"Error: {self.msg}"


class CustomZero(CustomErrorClass):
    def __init__(self, *args):
        self.msg = args[0] if args else None
        if args[0] == 'деление на ноль!!!':
            self.msg = "ошибка: деление невозможно!!!"
            print(self.msg)
            from sys import exit
            exit(1)


class CustomValue(CustomErrorClass):
    def __init__(self, *args):
        self.msg = args[0] if args else None
        if args[0] == 'не число!!!':
            self.msg = "ошибка: нечисловой аргумент"
            print(self.msg)
            from sys import exit
            exit(1)


if __name__ == '__main__':
    def zerodiv():
        a = input('a=')
        print('делим на:')
        b = input('b=')
        if not a.isdigit() or not b.isdigit():
            raise CustomValue("не число!!!")
        if int(b) == 0:
            raise CustomZero('деление на ноль!!!')
        res = int(a)/int(b)
        return f"{res}"
    print(zerodiv())


