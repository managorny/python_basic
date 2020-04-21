"""
6. *Реализовать структуру данных «Товары».
Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
"""

input("Введите данные о товаре, нажмите Enter для продолжения.\n")
n = 0
main_list = []
product = True
while product:
    n = n + 1
    name = input("Введите название товара\n")
    price = input("Введите цену товара\n")
    count = input("Введите количество товара\n")
    unit = input("Введите единицу измерения кол-ва товара\n")
    while True:
        price, count = float(price), float(count)
        break
    main_list.append((n, {"название": name, "цена": price, "количество": count, "ед": unit}))
    step = input("Нажмите Enter для продолжения или 0 для завершения\n")
    if step.isdigit():
        step = int(step)
        if step == 0:
            product = False
    else:
        continue
print(f'\nСписок\n{main_list}\nДалее построчно')
print('\n'.join(map(str, main_list)))   # для удобства чтения

# Собираем аналитику (вынес отдельно, чтобы если нужно можно было запускать отдельно, потом)
name_an = []
price_an = []
count_an = []
unit_an = []
for i in main_list:
    k = i[1]
    name_an = name_an + [k.get('название')]
    price_an = price_an + [k.get('цена')]
    count_an = count_an + [k.get('количество')]
    unit_an = unit_an + [k.get('ед')]
main_dict = {"название": list(set(name_an)), "цена": list(set(price_an)), "количество": list(set(count_an)),
             "ед": list(set(unit_an))}
print(f'\nАнализ, словарь\n{main_dict}\nДалее построчно')
for item in main_dict.items():
    print(item)
