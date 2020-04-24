"""
6. Реализовать два небольших скрипта:
а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
"""

from itertools import count, cycle
from time import sleep

# a)
start = 1
for i in count(start):
    print(int(i))
    # sleep(1)

# b)
lst = [1, 2, 3]
for i in cycle(lst):
    print(i)
    # sleep(1)
