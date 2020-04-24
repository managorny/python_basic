"""
6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.

Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки,
но каждое слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().
"""

import re


def int_func(w):
    a = w.split(' ')
    for i in a:
        if i.islower() and re.search(r'[a-z]', i):  # 97 < ord(i) <= 122
            print("good")
        else:
            error = "Not a lowercase or letters"
            return error

    return w.title()


print(int_func('lorem ipsum dolor sit amet, consectetur adipiscing elit.'))
