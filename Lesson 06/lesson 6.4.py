# инициализация родительского класса
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = int(speed)
        self.color = str(color)
        self.name = str(name)
        self.is_police = bool(is_police)

    def go(self):
        print('Машина едет')

    def stop(self):
        print('Машина стоит')

    def turn(self, direction):
        print(f'Машина едет {direction}')

    def show_speed(self):
        print(f'Машина едет со скоростью: {self.speed}')


# инициализация классов наследников
class TownCar(Car):
    # переписываем родительский метод
    def show_speed(self):
        if self.speed > 60:
            print(f'Машина едет со скоростью: {self.speed} - превышение скорости')
        else:
            print(f'Машина едет со скоростью: {self.speed}')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Машина едет со скоростью: {self.speed} - превышение скорости')
        else:
            print(f'Машина едет со скоростью: {self.speed}')


class PoliceCar(Car):
    pass


# создание экземпляров класса, работа с атрибутами и методами
sport_car = SportCar(120, 'red', 'mazda', False)
sport_car.go()

work_car = WorkCar(20, 'blue', 'ford', False)
work_car.show_speed()
work_car.speed = 60
work_car.show_speed()

town_car = TownCar(60, 'green', 'toyota', False)
town_car.go()
town_car.turn('налево')
town_car.stop()