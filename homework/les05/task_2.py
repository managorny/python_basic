"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""


with open('task_2.txt', 'r', encoding='UTF-8') as file:
    a = []
    for itm in file:
        a.append(itm)
    print(f'Кол-во строк: {len(a)}')
    for i in a:
        p = a.index(i) + 1
        i = i.split()
        print(f'Количество слов строки {p} - {len(i)}')
