"""
2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.

Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта,
проверить на практике работу декоратора @property.
"""
from abc import ABC, abstractmethod


class Clothes(ABC):

    @abstractmethod
    def __init__(self):
        self.name = ''

    @abstractmethod
    def total_tissue(self) -> str:
        pass


class Coat(Clothes):
    def __init__(self, v):
        super().__init__()
        self.v = v
        self.name = 'Пальто'

    @property
    def total_tissue(self):
        return f'Расход ткани на тип одежды "{self.name}" - {round((self.v / 6.5) + 0.5, 2)}'


class Costume(Clothes):
    def __init__(self, h):
        super().__init__()
        self.h = h
        self.name = 'Костюм'

    @property
    def total_tissue(self):
        return f'Расход ткани на тип одежды "{self.name}" - {round((self.h / 6.5) + 0.5, 2)}'


coat = Coat(v=0.44)
costume = Costume(h=1.8)

print(coat.total_tissue)
print(costume.total_tissue)

