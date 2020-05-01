"""
5. Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.”
Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки'


class Pen:
    def __init__(self):
        super().__init__()
        self.title = 'Ручка'

    def draw(self):
        return f'Запуск отрисовки. {self.title}'


class Pencil:
    def __init__(self):
        super().__init__()
        self.title = 'Карандаш'

    def draw(self):
        return f'Запуск отрисовки. {self.title}'


class Handle:
    def __init__(self):
        super().__init__()
        self.title = 'Маркер'

    def draw(self):
        return f'Запуск отрисовки. {self.title}'


my_pen = Pen()
my_pencil = Pencil()
my_handle = Handle()

print(my_pen.draw())
print(my_pencil.draw())
print(my_handle.draw())
