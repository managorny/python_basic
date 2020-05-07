"""7. Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""


class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.z = 'a + b * j'  # 'a + b * i'

    # def __init__(self, complex_number: str):
    #     self.complex_number = complex(complex_number)

    def __add__(self, other):
        z = f'{(self.a + other.a)}+{(self.b + other.b)}j'
        return complex(z)

    # def __add__(self, other):
    #     return self.complex_number + other.complex_number

    def __mul__(self, other):
        z = f'{self.a * other.a - (self.b * other.b)}+{self.b * other.a + self.a * other.b}j'
        return complex(z)

    # def __mul__(self, other):
    #     return self.complex_number * other.complex_number


complex_num1 = ComplexNumber(2, 7)
complex_num2 = ComplexNumber(3, -2)

# complex_num1 = ComplexNumber('2+7j')
# complex_num2 = ComplexNumber('3-2j')

print(complex_num1 + complex_num2)
print(complex_num1 * complex_num2)
