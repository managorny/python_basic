"""
2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
 имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""


def func_info(dict_in):
    return dict_in

print("Заполните данные")
my_dict = {}
my_dict["Имя"] = input("Имя\n")
my_dict["Фамилия"] = input("Фамилия\n")
my_dict["Год рождения"] = input("Год рождения\n")
my_dict["Город проживания"] = input("Город проживания\n")
my_dict["Email"] = input("Email\n")
my_dict["Телефон"] = input("Телефон\n")

print(func_info(my_dict))