# инициализация переменных
count, words = 0, 0
# открытие созданного ранее файла
with open(r'text/задание 2.txt', encoding='UTF8') as f:
    for using_line in f:
        count += 1      # подсчет строк
        words += len(using_line.split())    # подсчет слов
        print(f'{count} строка, слов: {len(using_line.split())}, содержание: ' + using_line.split('\n')[0])
print(f'\nВсего строк: {count}, всего слов: {words}')   # вывод данных
