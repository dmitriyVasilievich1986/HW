# инициализация класса
class Date:
    """класс принимает дату в формате 'dd-mm-yyyy'
        первый метод возвращает список целочисленных значений
        второй метод проверяет список на соответствие критериям даты"""
    def __init__(self, date):
        self.date = date

    @classmethod
    def date_init(cls, date):
        using_date = date.split('-')
        return list(map(int, using_date))

    @staticmethod
    def check(date):
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if date[1] < 1 or date[1] > 12 or date[0] < 0 or date[0] > days[date[1] - 1]:
            print('Введена неверная дата')
        else:
            print('Введена верная дата')


# инициализация экземпляра класса
date = Date('01-01-2020')
# работа с методами класса
Date.check(date.date_init(date.date))
Date.check(Date.date_init('30-02-2020'))