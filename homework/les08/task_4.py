"""
4. Начните работу над проектом «Склад оргтехники».
Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
"""


class Warehouse:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.printers = []
        self.scanners = []
        self.xerox = []
        self.other = []


class OfficeEq:
    def __init__(self, type_of, count, manufacturer, name, department):
        self.type_of = type_of
        self.count = count
        self.manufacturer = manufacturer
        self.name = name
        self.department = department
        self.my_dict = {"type_of": self.type_of, "name": self.name,
                        "count": self.count, "manufacturer": self.manufacturer,
                        "department": self.department}

    def __str__(self):
        return f'{self.my_dict}'

class Printer(OfficeEq):
    def __init__(self, type_of, count, manufacturer, name, department, color: bool, format_paper):
        super().__init__(type_of, count, manufacturer, name, department)
        self.color = color
        self.format_paper = format_paper
        self.my_dict = {"type_of": self.type_of, "name": self.name,
                        "count": self.count, "manufacturer": self.manufacturer,
                        "department": self.department, "color": color, "format_paper": format_paper}


class Scanner(OfficeEq):
    def __init__(self, type_of, count, manufacturer, name, department, size, copy: bool):
        super().__init__(type_of, count, manufacturer, name, department)
        self.size = size
        self.copy = copy
        self.my_dict = {"type_of": self.type_of, "name": self.name,
                        "count": self.count, "manufacturer": self.manufacturer,
                        "department": self.department, "size": self.size, "copy": self.copy}


class Xerox(OfficeEq):
    def __init__(self, type_of, count, manufacturer, name, department, size, copy: bool, color: bool, format_paper):
        super().__init__(type_of, count, manufacturer, name, department)
        self.size = size
        self.copy = copy
        self.color = color
        self.format_paper = format_paper
        self.my_dict = {"type_of": self.type_of, "name": self.name,
                        "count": self.count, "manufacturer": self.manufacturer,
                        "department": self.department, "size": self.size, "copy": self.copy,
                        "color": color, "format_paper": format_paper}
