"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна
корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


# 1 вариант
class MyException:
    def __init__(self, number):
        self.number = number

    def __truediv__(self, other):
        return MyException(self.number / other.number) if other.number != 0 else f'Происходит деление на 0, операция невозможна'

    def __str__(self):
        return str(self.number)


a = float(input("Введите делимое\n"))
b = float(input("Введите делитель\n"))
print(MyException(a) / MyException(b))


# 2 вариант
class MyException2Error(Exception):
    def __init__(self, text):
        self.text = text


class MyDivision:
    def __init__(self, dividend, divider):
        self.dividend = dividend
        self.divider = divider

    @classmethod
    def division(cls, dividend, divider):
        if divider == 0:
            raise MyException2Error('Происходит деление на 0, операция невозможна')
        else:
            return dividend / divider


a = float(input("Введите делимое\n"))
b = float(input("Введите делитель\n"))

print(MyDivision.division(a, b))
