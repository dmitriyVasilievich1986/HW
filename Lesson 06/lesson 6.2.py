# инициализация класса
class Road:
    # конструктор класса, принимает длину и ширину
    def __init__(self, length, width):
        self._length = length
        self._width = width

    # метод класса, расчитывает массу асфальта
    def mass(self, height):
        return self._length * self._width * 25 * height // 1000


# создание экземпляра класса
road = Road(20, 5000)
# вызов метода класса
print(f'{road.mass(5)} тонн')
