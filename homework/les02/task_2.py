"""
2. Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""

a = input("Введите элементы списка через пробел: \n")

a = a.split(' ')
print(a)
k = 0
i = 0
for k in range(len(a) // 2):
    print(len(a) // 2)
    a[i], a[i + 1] = a[i + 1], a[i]
    i += 2
print(a)
