# импорт библиотеки
import time
# инициализация списка чисел
numbers = [1, 15, 20, 7, 8, 99]
# сохранение списка в новый файл
with open(r'text\задание 5.txt', 'w') as f:
    for a in numbers:
        f.write(f'{a} ')
    print('Сохранение файла...')
    time.sleep(1)
print('Чтение файла...')
time.sleep(1)
# чтение файла
with open(r'text\задание 5.txt') as f:
    line = f.read()
    result = 0
    for a in line.split():
        result += int(a)
    print(f'Сумма всех чисел = {result}')       # вывод суммы
