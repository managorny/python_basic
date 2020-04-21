"""
4. Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y.
Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
"""


# С оператором **
def my_func(x, y):
    try:
        x = float(x)
        y = int(y)
        if x < 0:
            print("x не действительное положительное")
        elif y > 0:
            print("y не целое отрицательное")
        else:
            return x ** y
    except ValueError:
        print("Не те числа")
    except TypeError:
        print("Не те числа")


print(my_func(3, -2))


# Без оператора ** , через цикл
def my_func(x, y):
    try:
        x = float(x)
        y = int(y)
        if x < 0:
            print("x не действительное положительное")
        elif y > 0:
            print("y не целое отрицательное")
        else:
            z = 0
            for i in range(y * -1):
                if i > 0:
                    z = (z * x)
                else:
                    z = x
            z = 1 / z
            return z
    except ValueError:
        print("Не те числа")
    except TypeError:
        print("Не те числа")


print(my_func(3, -2))
