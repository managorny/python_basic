"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода.
Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""


class Date:
    def __init__(self, date_in: str):
        self.date_in = date_in
    # Вариант если преобразовывать в строку нужного формата
    # def __init__(self, day, month, year):
    #     date = '%s-%s-%s' % (day, month, year)

    @classmethod
    def date_str_to_int(cls, date_in):
        date_in = date_in.split('-')
        day = int(date_in[0])
        month = int(date_in[1])
        year = int(date_in[2])
        return day, month, year

        # my_date = []
        # for i in date_in.split('-'):
        #     my_date.append(i)
        # return my_date

    @staticmethod
    def validate_date(date_in):
        day, month, year = Date.date_str_to_int(date_in)
        if year < 0 or year > 2020:
            return f'Не верно указан год'
        elif 1 > month or month > 12:
            return f'Не верно указан месяц'
        elif month in (4, 6, 9, 11):
            if 1 > day or day > 30:
                return f'Не верно указана дата'
        elif month in (1, 3, 5, 7, 8, 10, 12):
            if 1 > day or day > 31:
                return f'Не верно указана дата'
        elif month == 2:
            if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
                if 1 > day or day > 28:
                    return f'Не верно указана дата'
            else:
                if 1 > day or day > 29:
                    return f'Не верно указана дата'

        return f'Введенные числа даты корректны'


print(Date.date_str_to_int('12-12-2012'))
print(Date.validate_date('12-12-2012'))
print(Date.validate_date('30-02-2020'))

