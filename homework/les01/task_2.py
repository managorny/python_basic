"""
2. Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
"""
time = input("Введите время в секундах\n")

if time.isdigit():
    time = int(time)
    print(time)
    if time > 0:
        seconds = time % 60
        minutes = (time // 60) % 60
        hours = time // (60 ** 2)
        print(f'{hours}:{minutes}:{seconds}')
else:
    print("Введите корректное число")
