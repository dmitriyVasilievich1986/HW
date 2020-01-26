# инициализация класса
class Cell:
    # конструктор класса
    def __init__(self, count):
        self.count = int(count)

    # инициализация методов класса
    def __add__(self, other):
        return Cell(self.count + other.count)

    def __mul__(self, other):
        return Cell(self.count * other.count)

    def __truediv__(self, other):
        return Cell(self.count // other.count)

    def __sub__(self, other):
        if self.count > other.count:
            return Cell(self.count - other.count)
        else:
            return 'Операция невыполнима'

    def __str__(self):
        return f'Общее число клеток = {self.count}'

    # метод возвращающий визуальную клетку
    def make_order(self, cell, count):      # принимает экземпляр класса и колво ед в ряду
        line = []
        for a in range(1, cell.count + cell.count // count + 1):
            line.append('*' if not a % (count + 1) == 0 else '\n')
        return ''.join(line)


# создание экземпляров класса
cell1 = Cell(100)
cell2 = Cell(300)
# работа с методами класса
print(cell1 + cell2)
print(cell1 - cell2)
print(cell2 - cell1)
print(cell1 * cell2)
print(cell1 / cell2)
print(cell2 / cell1)
# реализация визуального вывода информации о классе
print('Визуальный вывод:')
print(cell1.make_order(Cell(97), 25))
