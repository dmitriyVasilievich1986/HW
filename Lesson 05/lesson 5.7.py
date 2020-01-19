# импорт библиотеки
import json
# инициализация списков
firms = []
companies = {}
# чтение ранее созданного файла
with open(r'text/Задание 7.txt', encoding='UTF=8') as f:
    for lines in f:
        companies[lines.split()[0]] = int(lines.split()[2]) - int(lines.split()[3])     # добавление данных в словарь
# добавление данных в список
firms.append(companies)
firms.append({'Средний доход': 0})
count = 0
# подсчет средних доходов
for item in firms[0]:
    if firms[0][item] > 0:
        firms[1]['Средний доход'] += firms[0][item]
        count += 1
# добавление в список словаря средних доходов
firms[1]['Средний доход'] //= count
print(firms)
# запись списка в json формат
with open('text/Задание 8.json', 'w', encoding='UTF8') as f:
    json.dump(firms, f)

