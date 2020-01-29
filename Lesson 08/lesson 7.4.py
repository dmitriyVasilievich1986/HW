# импорт библиотек
from abc import ABC, abstractmethod


# region инициализация классов
class Storage:
    def _valid(self, valid_class, valid_count):
        if not type(valid_class) is Printer and not type(valid_class) is Scanner and not type(valid_class) is Xerox:
            return True
        if not type(valid_count) is int:
            return True
        return False

    def __init__(self):
        self.position = {}

    def __str__(self):
        line = 'На складе содержится следующая техника:\n'
        for a in self.position.keys():
            line += a + ':\n'
            for x in self.position[a]:
                line += f'\t{str(list(x.keys())[0])}'
                line += f'\t кол-во: {str(list(x.values())[0])}\n'
        return line

    def __add__(self, other):
        if self._valid(other[0], other[1]):
            return
        if not list(self.position.keys()).count(other[0].name):
            self.position[other[0].name] = []
        if [item for sub in self.position[other[0].name] for item in sub.keys()].count(other[1]) == 0:
            self.position[other[0].name].append({other[0]: other[1]})
        return

    def __sub__(self, other):
        if self._valid(other[0], other[1]):
            return
        if not list(self.position.keys()).count(other[0].name) or not len([x for x in self.position[other[0].name] if list(x.keys())[0].model == other[0].model]):
            print('Указанной модели нет на складе')
            return
        else:
            if [list(x.values())[0] for x in self.position[other[0].name] if list(x.keys())[0].model == other[0].model][0] < other[1]:
                print('На складе недостаточно техники')
                return
            else:
                for x in self.position[other[0].name]:
                    if list(x.keys())[0].model == other[0].model:
                        x[list(x.keys())[0]] -= other[1]
        return

    def __getitem__(self, item):
        return self.position[item[0]][item[1]]


class Machine(ABC):
    def __init__(self, model, price):
        self.model = str(model)
        self.price = int(price)

    def __str__(self):
        return f'Модель: {self.model}, Цена: {self.price}'

    @abstractmethod
    def functional(self):
        pass


class Printer(Machine):
    def __init__(self, model, price):
        super().__init__(model, price)
        self.name = 'Принтер'

    def functional(self):
        print('Печатает...')


class Scanner(Machine):
    def __init__(self, model, price):
        super().__init__(model, price)
        self.name = 'Сканер'

    def functional(self):
        print('Сканирует...')


class Xerox(Machine):
    def __init__(self, model, price):
        super().__init__(model, price)
        self.name = 'Ксерокс'

    def functional(self):
        print('Копирует...')


# endregion


# инициализация экземпляра класса
storage = Storage()
storage + (Printer('A100', 5000), 5)
storage + (Printer('A101', 5500), 3)
storage + (Scanner('B1150', 7500), 1)
print(storage)

storage - (Printer('A100', 5000), 2)
print(storage)

storage + (Xerox('sadas', 'asdas'))
print(storage)
