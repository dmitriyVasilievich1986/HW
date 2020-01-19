# инициализация переменных
wage = 0
surname = {}
# чтение данных из файла
with open(r'text/Задание 3.txt', encoding='UTF=8') as f:
    for lines in f:
        surname[lines.split()[0]] = int(lines.split()[1])   # добавление данных в словарь
# проверка на соответсвие условию
if min(surname.values()) < 20000:
    print('Сотруднки с окладом менее 20000:')
# вывод списка сотрудников с окладом менее 20000
for item in surname.keys():
    if surname[item] < 20000:
        print(f'{item} - {surname[item]}')
    wage += surname[item]   # сумма всех зп
# вывод средней зп
print(f'\nСредний оклад: {wage//len(surname)}')
