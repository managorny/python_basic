"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def my_func(x, y):
    return x / y


try:
    print("Укажите числа для операции деления")
    first_num = float(input("Введите первое число: "))
    second_num = float(input("Введите второе число: "))
    print(f'Результат: {round(my_func(first_num,second_num), 2)}')
except ZeroDivisionError:
    print("Вы пытаетесь делить на 0. Так нельзя")
except TypeError:
    print("Вы точно вводите числа?")
except ValueError:
    print("Вы точно вводите числа?")
