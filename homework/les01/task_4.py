"""
4. Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""
try:
    number = int(input("Введите целое положительное число\n"))
    if number == 0:
        print("Вы ввели 0")
    elif number < 0:
        print("Вы ввели отрицательное число")
    else:
        digit = 0
        while number > 0:
            checking = number % 10
            number = number // 10
            if checking > digit:
                digit = checking
        print(digit)
except ValueError:
    print("Ошибка: введите целое положительное число")
