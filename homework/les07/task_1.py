"""
1. Реализовать класс Matrix (матрица).
Обеспечить перегрузку конструктора класса (метод init()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно —
первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        for i in self.data:
            return '\n'.join([''.join(['%s\t' % i for i in row]) for row in self.data])

    def __add__(self, other):
        result = []
        numbers = []
        for i in range(len(self.data)):
            for k in range(len(self.data[0])):
                my_sum = other.data[i][k] + self.data[i][k]
                numbers.append(my_sum)
                if len(numbers) == len(self.data[0]):
                    result.append(numbers)
                    numbers = []
        return Matrix(result)
    # для разных размеров матриц (но без добавления доп. списка, который у большей матрицы)
    # def __add__(self, other):
    #     return Matrix(list(map(
    #                     lambda x, y: list(map(lambda z, w: z + w, x, y)),
    #                     self.data, other.data)))


a = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = Matrix([[2, 3, 4], [4, 6, 7], [4, 6, 7]])

print(a + b)

