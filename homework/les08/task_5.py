"""
5. Продолжить работу над первым заданием.
Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
можно использовать любую подходящую структуру, например словарь.
"""

from homework.les08.task_4 import Warehouse, OfficeEq, Printer, Scanner, Xerox

my_warehouse = Warehouse(name="Мой склад", address='Москва')


class NotNumError(Exception):
    def __init__(self, text):
        self.text = text


class MyMethods:
    @staticmethod
    def to_warehouse(a):
        while True:
            try:
                count_of_new_products = int(input("Введите кол-во товаров, которые хотите добавить на склад\n"))
            except ValueError:
                print("Not a number")
            else:
                break
        # print(dir(new_product))  # думал поопробовать брать список аргументов из класса
        for i in range(1, count_of_new_products + 1):
            name = input(f'Введите название товара {i}\n')
            while True:
                try:
                    count = input("Введите кол-во товара\n")
                    if count.isdigit():
                        count = int(count)
                        break
                    else:
                        raise NotNumError('Not a number')
                except NotNumError as err:
                    print(err)
            manufacturer = input("Введите производителя\n")
            departament = input("Введите департамент, в который отправить товар\n")
            if a == 'p':
                while True:
                    try:
                        color = bool(int(input("Принтер цветной? (1 или 0)\n")))
                    except ValueError:
                        print("Not 1 or 0")
                    else:
                        break
                format_paper = input("Введите размеры бумаги, которые принимает принтер\n")
                new_product = Printer(type_of='Принтер', name=name, count=count, manufacturer=manufacturer,
                                      department=departament, color=color, format_paper=format_paper)
                my_warehouse.printers.append(new_product)
            elif a == 's':
                size = input("Введите разер сканера\n")
                while True:
                    try:
                        copy = bool(int(input("Сканер умеет копировать? (1 или 0)\n")))
                    except ValueError:
                        print("Not 1 or 0")
                    else:
                        break
                new_product = Scanner(type_of='Сканер', name=name, count=count, manufacturer=manufacturer,
                                      department=departament, size=size, copy=copy)
                my_warehouse.scanners.append(new_product)
            elif a == 'x':
                while True:
                    try:
                        color = bool(int(input("принтер в ксероксе цветной? (1 или 0)\n")))
                    except ValueError:
                        print("Not 1 or 0")
                    else:
                        break
                format_paper = input("Введите размеры бумаги, которые принимает принтер ксерокса\n")
                size = input("Введите разер сканера в ксероксе\n")
                while True:
                    try:
                        copy = bool(int(input("Сканер ксерокса умеет копировать? (1 или 0)\n")))
                    except ValueError:
                        print("Not 1 or 0")
                    else:
                        break
                new_product = Xerox(type_of='Ксерокс', name=name, count=count, manufacturer=manufacturer,
                                    department=departament, color=color, format_paper=format_paper,
                                    size=size, copy=copy)
                my_warehouse.xerox.append(new_product)
            elif a == 'o':
                type_of = (input("Введите тип товара\n"))
                new_product = OfficeEq(type_of=type_of, name=name, count=count, manufacturer=manufacturer,
                                       department=departament)
                my_warehouse.other.append(new_product)

    @staticmethod
    def print_warehouse_printers():
        print('\n'.join(str(i) for i in my_warehouse.printers))

    @staticmethod
    def print_warehouse_scanners():
        print('\n'.join(str(i) for i in my_warehouse.scanners))

    @staticmethod
    def print_warehouse_xerox():
        print('\n'.join(str(i) for i in my_warehouse.xerox))

    @staticmethod
    def print_warehouse_other():
        print('\n'.join(str(i) for i in my_warehouse.other))


if __name__ == '__main__':
    step = True
    while step:
        choice = input("Какой тип товара хотите добавить? (p - принтер, s - сканнер, x - ксерокс, o - другое)\n")
        if choice != 'p' and choice != 's' and choice != 'x' and choice != 'o':
            print("Введены не верные данные")
            step = int(input("Продолжить? 1 - Да, 0 - Нет\n"))
        else:
            MyMethods.to_warehouse(choice)

        if choice == 'p':
            MyMethods.print_warehouse_printers()
            step = False
        elif choice == 's':
            MyMethods.print_warehouse_scanners()
            step = False
        elif choice == 'x':
            MyMethods.print_warehouse_xerox()
            step = False
        elif choice == 'o':
            MyMethods.print_warehouse_other()
            step = False
    else:
        print("Выход")
