# импорт библиотек
from abc import ABC, abstractmethod


# region инициализация классов
class Storage:
    def __init__(self):
        self.list_of_machine = []

    def __str__(self):
        return f'Склад содержит следующую технику: '.join(self.list_of_machine)

    def __add__(self, other):
        self.list_of_machine.append(other)
        return self.list_of_machine[-1]

    def __getitem__(self, item):
        return self.list_of_machine[item]


class Machine(ABC):
    def __init__(self, model, price):
        self.model = model
        self.price = price

    @abstractmethod
    def functional(self):
        pass


class Printer(Machine):
    def functional(self):
        print('Печатает...')


class Scanner(Machine):
    def functional(self):
        print('Сканирует...')


class Xerox(Machine):
    def functional(self):
        print('Копирует...')
# endregion


# инициализация экземпляра класса
storage = Storage()
