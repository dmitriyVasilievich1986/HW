# инициализация родительского класса
class Stationery:
    def __init__(self, title):
        self.title = str(title)

    def draw(self):
        print(f'Рисуем картину {self.title}')


# инициализация классов наследников
class Pen(Stationery):
    def draw(self):
        print(f'Рисуем ручкой картину {self.title}')


class Pencil(Stationery):
    def draw(self):
        print(f'Рисуем карандашом картину {self.title}')


class Handle(Stationery):
    def draw(self):
        print(f'Рисуем маркером картину {self.title}')


# создание экземпляров класса
all_class = [Stationery('untitled'), Pen('untitled2'), Pencil('untitled3'), Handle('untitled4')]

# вызов метода во всех классах
for a in all_class:
    a.draw()
