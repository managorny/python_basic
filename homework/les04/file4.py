"""
Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать итоговый массив чисел, соответствующих требованию.
Элементы вывести в порядке их следования в исходном списке.
Для выполнения задания обязательно использовать генератор.
"""

from itertools import repeat

# TODO доделать

my_list = [1, 2, 3, 4, 5, 6, 4, 4, 5]
new_list = []
for i in range(len(my_list) - 1):
    for k in range(i + 1, len(my_list)):
        if my_list[i] == my_list[k]:
            break
        else:
            new_list.append(my_list[k])
print(new_list)
