class Stationery:
    title = ""

    def __init__(self, title: str) -> None:
        self.title = title

    def draw(self) -> None:
        print("Запуск отрисовки")


# определите классы ниже согласно условий задания
class Pen(Stationery):
    def draw(self) -> None:
        print(f'{Pen.__name__}: приступил к отрисовке объекта "{self.title}"')
class Pencil(Stationery):

    def draw(self) -> None:
        Stationery.draw(Stationery)
        print(f'{Pencil.__name__}: приступил к отрисовке объекта "{self.title}"')
class Handle(Stationery):
    def draw(self) -> None:
        print(f'{Handle.__name__}: приступил к отрисовке объекта "{self.title}"')


if __name__ == '__main__':
    pen = Pen('Ручка')
    pencil = Pencil('Карандаш')
    handle = Handle('Маркер')
    pen.draw()  # Pen: приступил к отрисовке объекта "Ручка"
    handle.draw()  # Handle: приступил к отрисовке объекта "Маркер"
    pencil.draw()  # Пример вывода ниже в многострочном комментарии
    """
    Запуск отрисовки
    Pencil: приступил к отрисовке объекта "Карандаш"
    """
