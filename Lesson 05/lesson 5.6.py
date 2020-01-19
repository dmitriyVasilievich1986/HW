# импорт библиотеки
import time
# инициализация словаря
faculty = {}
# открытие созданного ранее файла
with open(r'text\задание 6.txt', encoding='UTF8') as f:
    for lines in f:
        # убираем лишние знаки из строки
        using_lines = lines.lower().replace(':', ' ')
        using_lines = using_lines.lower().replace('(лаб)', ' ')
        using_lines = using_lines.lower().replace('(л)', ' ')
        using_lines = using_lines.lower().replace('(пр)', ' ')
        using_lines = using_lines.lower().replace(',', ' ')
        using_lines = using_lines.lower().replace('.', ' ')
        using_lines = using_lines.lower().replace('—', ' ')
        using_lines = using_lines.lower().replace('-', ' ')
        hours = 0
        # подсчет часов для каждого зания
        for a in using_lines.split():
            try:
                hours += int(a)
            except ValueError:
                time.sleep(.001)
        faculty[using_lines.split()[0]] = hours
# вывод словаря
print(faculty)
