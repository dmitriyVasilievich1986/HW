# открытие созданного ранее файла
with open(r'text\задание 4.txt', encoding='UTF8') as f:
    for lines in f:
        using_lines = lines.lower().replace('one', 'один')              # заменяем
        using_lines = using_lines.lower().replace('two', 'два')         # английские
        using_lines = using_lines.lower().replace('three', 'три')       # слова на
        using_lines = using_lines.lower().replace('four', 'четыре')     # русские
        # запись измененной строки в файл
        with open(r'text/задание 4 результат.txt', 'a') as file:
            file.write(using_lines)
