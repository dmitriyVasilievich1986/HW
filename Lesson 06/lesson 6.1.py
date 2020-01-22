# импорт библиотек
import time
from itertools import cycle


# инициализация собственного класса
class TrafficLight:
    def __init__(self):
        self.__color = {'красный': 7, 'желтый': 2, 'зеленый': 1}        # цвет светофора
        self._backup = ['красный', 'желтый', 'зеленый']                 # для проверки правильности

    # метод работы светофора
    def running(self):
        for a in cycle(enumerate(self.__color.keys())):
            if a[0] >= len(self._backup) or not self._backup[a[0]] == a[1]:     # проверка последовательности
                print('Нарушена последовательность работы светофора')           # работы светофора
                break
            print(f'Горит {a[1]} цвет')                         # если все нормально
            time.sleep(self.__color[a[1]])                      # то светофор горит


# инициализация элемента класса
tl = TrafficLight()
# вмешательство в последовательность работы метода
tl._TrafficLight__color['синий'] = 5
# запуск метода
tl.running()
