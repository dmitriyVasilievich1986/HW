# инициализация бесконечного цикла ввода строк
while 1:
    new_line = input('Введите строку для записи: ')
    if(new_line == '' or new_line == ' '):              # выход если строка пучтая
        break
    with open(r'text/Задание 1.txt', 'a') as f:         # запись строки в файл
        f.writelines(new_line + '\n')
