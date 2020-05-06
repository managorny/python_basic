"""
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.

Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.

Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.

Пример json-объекта:

[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджеры контекста.
"""

import json

a = []
with open('task_7.txt', 'r') as file:
    for i in file:
        a.append(i)

profit = 0
count_of_company = 0
d = {}
e = {}
for i in a:     # вынес отдельно, чтобы не держать файл открытым.
    b = i.split(' ')
    d[b[0]] = b[2]
    count_of_company += 1
    if int(b[3]) > int(b[2]):
        continue
    else:
        profit += int(b[2])
e['average_profit'] = profit / count_of_company

z = [d, e]
print(z)
with open('task_7.json', 'w') as file:
    json.dump(z, file)

with open('task_7.json', 'r') as file:
    print(json.load(file))