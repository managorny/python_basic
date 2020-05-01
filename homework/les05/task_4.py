"""
4. Создать (не программно) текстовый файл со следующим содержимым:

One — 1
Two — 2
Three — 3
Four — 4

Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

a = []
with open('task_4.txt', 'r') as file:
    for i in file:
        print(i)
        a.append(i)
    for i in a:
        x = i.split(' — ')
        if x[0] == "One":
            x[0] = 'Один'
        elif x[0] == "Two":
            x[0] = 'Два'
        elif x[0] == "Three":
            x[0] = 'Три'
        elif x[0] == "Four":
            x[0] = 'Четыре'
        with open('task_4_2.txt', 'a') as file2:
            file2.write(f'{x[0]} - {x[1]}')

with open('task_4_2.txt', 'r') as file2:
    print(file2.read())
