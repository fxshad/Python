from pprint import pprint
from task_11_4 import Xerox, Scanner, Printer
from task_11_6 import check_int_dekor


class Storage:
    __SPACE = 100
    _engage_space = 0

    def __init__(self):
        self.item_list = {}

    def check_engagement(self, eng_sp, vol, quan):
        """проверка свободного места на складе"""
        check = eng_sp + quan * vol
        if check > self.__SPACE:
            quan = (self.__SPACE - eng_sp)//vol
            print(f"на складе не достаточно места, будет принято только {quan} устройств")
            return quan
        else:
            return quan

    @check_int_dekor
    def app_item(self, item, quantity):
        """принимает устройство(а) на склад"""
        quantity = self.check_engagement(self._engage_space, item._volume, quantity)
        self._engage_space += quantity * item._volume
        self.category = item.__class__.__name__  # имя класса экз
        self.item_list.setdefault(self.category, [0])
        for i in range(quantity):
            self.item_list[self.category].append(item.name)
            self.item_list[self.category][0] += 1
        print(f"{quantity} {item.name} приняты на склад")

    @check_int_dekor
    def send_to(self, depart: str, item, quantity):
        """отправляет оргтехнику в отделения компании"""
        self.category = item.__class__.__name__
        self.remains = self.item_list[self.category].count(item.name)
        if self.remains < quantity:
            quantity = self.remains
            print(f"есть только {quantity} устройств модели {item.name}")
        for i in range(quantity):
            self.item_list[self.category].remove(item.name)
            self.item_list[self.category][0] -= 1
        print(f"{quantity} {item.name} были отправлены в {depart}")

    @property
    def show_storage_place(self):
        print(f"MAX space:{self.__SPACE}, engaged:{self._engage_space}")

    @property
    def show_storage_list(self):
        pprint(self.item_list)


if __name__ == '__main__':
    warehouse = Storage()
    p = Printer("Olivetti")
    p1 = Printer("Canon 1010")
    s = Scanner("SuperScan 9000")
    x = Xerox("Mega Copy`5000")
    warehouse.app_item(s, 3)
    warehouse.app_item(p, 4)
    warehouse.app_item(p1, 2)
    warehouse.show_storage_place
    warehouse.show_storage_list
    print()

    warehouse.send_to("Отдел продаж", p, 6)
    warehouse.app_item(x, 6)
    warehouse.show_storage_place
    warehouse.show_storage_list


