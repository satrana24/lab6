from random import *

def first():
    dictionary = {"Австрия": "Вена", "Бельгия": "Брюссель", "Великобритания": "Лондон",
                  "Германия": "Берлин", "Ирландия": "Дублин", "Лихтенштейн": "Вадуц", "Нидерладны": "Амстердам",
                  "Франция": "Париж", "Белоруссия": "Минск", "Болгария": "София", "Россия": "Москва",
                  "Чехия": "Прага", "Албания": "Тирана", "Босния и Герцеговина": "Сараево",
                  "Северная Македония": "Скопье", "Сербия": "Белград"}
    print(dictionary)

    country = input('Введите название страны, столицу которой хотите узнать: ')
    if country in dictionary:
        print(f'Столицей {country} является {dictionary[country]}')
    else:
        print('К сожалению, данной страны в списке нет')

    for key in sorted(dictionary):
        print(key, '-', dictionary[key])


def second():
    alph = {
        'а': 1, 'в': 1, 'е': 1, 'и': 1, 'н': 1, 'о': 1, 'р': 1, 'с': 1, 'т': 1,
        'б': 3, 'г': 3, 'ё': 3, 'ь': 3, 'я': 3,
        'д': 2, 'к': 2, 'л': 2, 'м': 2, 'у': 2, 'п': 2,
        'ж': 5, 'з': 5, 'х': 5, 'ц': 5, 'ч': 5,
        'й': 4, 'ы': 4,
        'ф': 10, 'щ': 10, 'ъ': 10,
        'ш': 8, 'э': 8, 'ю': 8
    }
    word = input('Введите слово: ')
    amount = 0
    for i in word:
        amount += alph[i.lower()]
    print(f'Сумма из всех букв вашего слова: {amount}')


def third():
    stud = {'Петров': [],
            'Иванов': [],
            'Лебедев': [],
            'Цзиньпин': [],
            'Абийбилаев': []}
    language = ['Английский', 'Немецкий', 'Китайский', 'Французский', 'Тайский']

    for i in stud:
        s = randint(0, 4)
        l = randint(0, 4)
        for j in range(s):
            l = randint(0, 4)
            if language[l] not in stud[i]:
                stud[i].append(language[l])
    print(stud)
    q = 0
    for i in language:
        for j in stud:
            if i in stud[j]:
                    q += 1
        print(f'Количество студентов, знающих {i}: {q}')
    q = 0

    second_name = []
    for i in stud:
        if 'Китайский' in stud[i]:
            q += 1
            second_name.append(i)
    print('Студенты, знающие китайский:', *sorted(second_name))

third()
