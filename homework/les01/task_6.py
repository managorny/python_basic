"""
6. Спортсмен занимается ежедневными пробежками.
В первый день его результат составил a километров.
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
"""
try:
    a = float(input("Введите кол-во км в первый день\n"))
    b = float(input("Введите ожидаемое общее кол-во км\n"))
    total = a
    i = 1
    print(f'Результат:\n{i}-й день: {total}')
    while total <= b:
        i += 1
        total = round(total + (total * 0.1), 2)
        print(f'{i}-й день: {total}')
    print(f'Ответ: на {i}-й день спортсмен достиг результата — не менее {b} км.')
except ValueError:
    print("Возможно вы вводите не числа")
