# импорт библиотек
from abc import ABC, abstractmethod
from functools import reduce


# инициализация класса родителя
class Clothes(ABC):
    # конструктор класса
    def __init__(self, name, size):
        self._name = str(name)
        self._size = int(size)

    # инициализация интерфейса
    @abstractmethod
    def cloth_consumption(self):
        pass

    def __str__(self):
        return f'{self._name}, на пошив необходимо {self.cloth_consumption} кв.метров'

    def __add__(self, other):
        return round(self.cloth_consumption + other.cloth_consumption, 2)


# инициализация класса наследника
class Suit(Clothes):
    @property
    def cloth_consumption(self):
        return 2 * self._size + 0.3


# инициализация класса наследника
class Coat(Clothes):

    @property
    def cloth_consumption(self):
        return round(self._size / 6.5 + 0.3, 2)


# создание экземпляров классов
all_clothes = [Suit('Костюм', 42), Coat('Пальто', 46)]
# вывод расход материала всех изделий
list(map(print, all_clothes))
# вывод расхода всех изделий в сумме
print('Полный расход материала = ', reduce(lambda a, b: a + b, all_clothes), 'кв.метров')
