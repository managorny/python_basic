"""
4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
Если в слово длинное, выводить только первые 10 букв в слове.
"""

a = input("Введите слова через пробел:\n")

a = a.split(' ')
k = 0
for i in a:
    k = k + 1
    print(f'{k}. {i[:10]}')