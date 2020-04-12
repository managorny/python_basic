"""
3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
"""
n = input("Введите число\n")

if n.isdigit():
    n_int = int(n)
    n_str = str(n)
    result = n_int + int(f'{n_str + n_str}') + int(f'{n_str + n_str + n_str}')
    print(result)
else:
    print("Введите целое положительное число")
