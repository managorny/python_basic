"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

from random import randint

size = 10
with open('task_5.txt', 'w') as file:
    for i in range(size):
        x = randint(1, 100)
        file.write(f'{x} ')

b = []
x = 0
with open('task_5.txt', 'r') as file:
    for i in file:
        b = i.split(' ')
for j in b:     # вынес отдельно, чтобы не держать файл открытым.
    if j == '':
        break
    else:
        j = float(j)
        x += j
print(x)
