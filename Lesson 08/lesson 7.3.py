# инициализация класса
class Is_Not_Number(Exception):
    """класс исключение для обработки ввода чисел"""

    def __str__(self):
        return 'Введена строка, введите число'


# инициализация списка
new_list = []

# инициализация бесконечного цикла ввода и проверки чисел
while 1:
    new_item = input('Введите число: ')
    if new_item.lower() == 'stop':
        break
    try:
        if not new_item.isnumeric():
            raise Is_Not_Number
        else:
            new_list.append(int(new_item))
    except Exception as err:
        print(err)

# вывод результата
print(f'Полученный список: {new_list}')
