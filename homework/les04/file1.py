"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""

from sys import argv


def func(a, b, c):
    try:
        salary = (float(a) * float(b)) + float(c)
    except ValueError:
        print("Не верный параметр")
    except TypeError:
        print("Не верный параметр")
    return salary


_, x, y, z = argv

print(func(x, y, z))
