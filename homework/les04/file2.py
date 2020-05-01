"""
2. Представлен список чисел.
Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
"""

from random import randint


def func(size):
    this_list = [randint(0, 100) for _ in range(size)]
    return this_list


my_list = func(10)
print(my_list)
new_list = [itm for itm in my_list if itm > my_list[my_list.index(itm) - 1]]
print(new_list)
