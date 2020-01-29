# инициализация класса
class Division_Zero(Exception):
    """класс исключение для обработки возможности деления на ноль"""
    def __str__(self):
        return 'Деление на 0 запрещено'


# инициализация функции деления, с обработкой исключений
def division(divider, dividend):
    try:
        if dividend == 0:
            raise Division_Zero
        print(divider // dividend)
    except Exception as err:
        print(err)


# вызов функции
division(int(input('Введите делимое число: ')), int(input('Введите делитель: ')))