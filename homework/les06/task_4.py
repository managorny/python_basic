"""
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
"""


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = bool(is_police)

    def go(self):
        if self.speed > 0:
            return f'Машина поехала/едет'

    def stop(self):
        if self.speed <= 0:
            return f'Машина остановилась'

    def turn(self, direction):
        if self.speed > 0:
            if direction == -1:
                return f'Машина повернула налево'
            if direction == 1:
                return f'Машина повернула направо'

    def show_speed(self):
        return f'Текущая скорость - {self.speed}'


class TownCar(Car):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def show_speed(self):
        if self.speed > 60:
            return f'Превышение скорости! Текущая скорость - {self.speed}'
        else:
            f'Текущая скорость - {self.speed}'


class SportCar(Car):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class WorkCar(Car):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def show_speed(self):
        if self.speed > 40:
            return f'Превышение скорости! Текущая скорость - {self.speed}'
        else:
            return f'Текущая скорость - {self.speed}'


class PoliceCar(Car):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


my_town_car = TownCar(speed=80, color='white', name='Городской автомобиль', is_police=False)
my_sport_car = SportCar(speed=120, color='red', name='Спортивный автомобиль', is_police=False)
my_work_car = WorkCar(speed=40, color='gray', name='Рабочий автомобиль', is_police=False)
my_police_car = PoliceCar(speed=80, color='blue-white', name='Полицейский автомобиль', is_police=True)

print(f'Скорость полицейской машины: {my_police_car.speed}')
print(f'Цвет спортивной машины: {my_sport_car.color}')
print(f'Рабочая машина - полицейская? {my_work_car.is_police}')
print(f'Чья скорость {my_town_car.speed}? Это - {my_town_car.name}')

print(f'{my_sport_car.name} - статус - {my_sport_car.go()}')

print(f'\nПокажи текущую скорость машины с именем: {my_work_car.name}')
print(f'{my_work_car.show_speed()}\n')

print(f'\nПокажи текущую скорость машины с именем: {my_town_car.name}')
print(f'{my_town_car.show_speed()}\n')

print(f'Машина "{my_sport_car.name}" - статус - {my_sport_car.turn(-1)}')
