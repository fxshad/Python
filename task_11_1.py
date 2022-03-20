from datetime import datetime


class Date:
    DATE = ()

    def __init__(self, str_date: str):
        if not isinstance(str_date, str):
            Date.DATE = 'None'
            print('need str, ', end=' ')
        elif str_date[2] != "-" or str_date[5] != "-":
            Date.DATE = 'None'
        else:
            Date.DATE = str_date
            self.__extract_numb()
            self.__validation(Date.DATE)

    def __str__(self):
        if Date.DATE == 'None':
            return f"error format: dd-mm-yyyy "
        else:
            return f"{str(Date.DATE[0]).zfill(2)}.{str(Date.DATE[1]).zfill(2)}.{Date.DATE[2]} это реальная дата "

    @classmethod
    def __extract_numb(cls):
        if len(cls.DATE) != 10:  # length check
            cls.DATE = 'None'
        else:
            try:
                d, m, y = map(int, (cls.DATE[0:2], cls.DATE[3:5], cls.DATE[6:11]))
                Date.DATE = (d, m, y)
            except ValueError:
                cls.DATE = 'None'

    @staticmethod
    def __validation(data):
        d, m, y = data
        try:
            datetime(y, m, d)
        except ValueError:
            print("impossible Date", end=' ')
            Date.DATE = 'None'
        return data


if __name__ == '__main__':
    d = "01-01-2000"
    e = 01.012000
    print(Date(d))
    print(Date.DATE, "tuple")
    print(Date(e))
    print(Date('22*12<2000'))
    print(Date('18806-1992'))
    d1 = Date("29-02-2020")
    print(d1)
    print(Date("12-13-1903"))
    print(Date("sdffdfdsdf"))

