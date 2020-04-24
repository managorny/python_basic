"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


def my_func(a, b, c):
    if b < a < c or b < c < a:
        d = a + c
    elif a < b < c or a < c < b:
        d = b + c
    else:
        d = a + b
    return d


print(my_func(20, 10, 40))
