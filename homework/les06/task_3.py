"""
3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь,
содержащий элементы: оклад и премия, например,
{"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
 и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных
(создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
"""


class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_full_name(self):
        return f'Полное имя: {self.name} {self.surname}'

    def get_total_income(self):
        return f'Доход с учетом премии: {self._income["wage"] + self._income["bonus"]}'


trying = Position(name='Ivan', surname='Petrov', position='manager', wage=100000, bonus=50000)

print(trying.name)
print(trying.surname)
print(trying.position)
print(trying._income)

print(trying.get_full_name())
print(trying.get_total_income())
