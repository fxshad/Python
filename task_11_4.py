class Storage:
    __SPACE = 100
    _engage_space = 0

    def __init__(self):
        self.item_list = {}

    def app_item(self):
        pass

    def send_to(self):
        pass


class OfficeEqp:
    name: str
    _volume = None
    _work = None

    def __init__(self, name):
        self.naming(name)

    def naming(self, name):
        """присваивает модель устройству"""
        self.name = name

    @property
    def show_info(self):
        """показывает свои характеристики"""
        print(f"Имя устройства: {self.name}, занимает места: {self._volume}, назначение: {self._work}")


class Printer(OfficeEqp):
    _volume = 3
    _work = "печать"


class Scanner(OfficeEqp):
    _volume = 2
    _work = "сканирование"


class Xerox(OfficeEqp):
    _volume = 5
    _work = "копирование"


if __name__ == '__main__':
    p = Printer("LaserJet2000")
    s = Scanner("HP Scanjet Pro")
    x = Xerox("Xerox Phaser 3020")
    s.show_info



