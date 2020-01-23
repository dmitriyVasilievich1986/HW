# инициализация класса родителя
class Worker:
    # конструктор класса
    def __init__(self, name, surname, position, wage, bonus):
        self.name = str(name)
        self.surname = str(surname)
        self.position = str(position)
        self._income = {'wage': int(wage), 'bonus': int(bonus)}


# инициализация класса наследника
class Position(Worker):
    # инициализация методов класаа
    def get_full_name(self):
        print(f'Ф.И. работника: {self.surname.title()} {self.name.title()}')

    def get_total_income(self):
        print(f'Полный доход сотрудника: {self._income["wage"] + self._income["bonus"]}')


# создание экземпляра класса
person = Position('Иван', 'Иванов', 'Рабочий', 10000, 20000)
# вызов методов класса
person.get_full_name()
person.get_total_income()
# вызов атрибута класса
person.position = 'некоторая должность'
print(f'Должность - {person.position}')
