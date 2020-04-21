"""
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел, то
вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
"""


def my_func(nums, p_sum):
    sums = 0
    for i in nums:
        try:
            i = float(i)
            sums += i
            if 'q' in nums:
                d = sums + p_sum
                next = False
                return d, next
        except TypeError:
            print("Похоже вы ввели не числа")
        except ValueError:
            print("Похоже вы ввели не числа")
    d = sums + p_sum
    next = True
    return d, next


old_sum = 0
next_step = True
while next_step:
    a = input("Введите числа \n")
    sum_num = a.split(' ')
    sum_final, next_step = my_func(sum_num, old_sum)
    print(sum_final)
    old_sum = sum_final
else:
    print("Программа завершена")
