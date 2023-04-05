# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной

#import csv #не пригодилось

def print_phonebook():
    data_file = open(phonebook_filename, 'r', encoding='utf-8')
    for line in data_file:
        if len(line) < 3: continue #пропускаем пустые строчки
        for item in line.strip().split(','):
            print(item, end='\t')
        print('')
    data_file.close()

def search_phonebook_by_phone():
    search_phonebook(phonebook_fields.index('Телефон'))

def search_phonebook(search_by = 0):
    look_for = input('Введите строку для поиска: ')
    search_result = []
    with open(phonebook_filename, 'r', encoding='utf-8') as data_file:
        for line in data_file:
            thisLine = line.strip().split(',')
            if str(thisLine[search_by]).strip().lower().find(look_for.lower()) != -1:
                search_result.append(thisLine)

    print(f'Найдено {len(search_result)} записей:')
    for line in search_result:
        print(line)

def append_record_to_phonebook():
    this_record = []
    for i in range(len(phonebook_fields)):
        this_record.append(input(f'Введите значение поля "{phonebook_fields[i]}": '))

    with open(phonebook_filename, 'a', encoding='utf-8') as data_file:
        data_file.write("\n" + ','.join(this_record) + "\n")

def export_to_txt():
    export_data = list()
    with open(phonebook_filename, 'r', encoding='utf-8') as data_file:
        for line in data_file:
            if len(line) < 3: continue
            export_data.append(dict(zip(phonebook_fields, line.strip().split(','))))

    with open(export_filename, 'w', encoding='utf-8') as export_file:
        for i in export_data:
            export_file.write(str(i)+'\n')


phonebook_filename = 'phonebook.csv'
export_filename = 'export.txt'
phonebook_fields = ('Фамилия', 'Имя', 'Телефон', 'Описание')

main_menu_items = [
#   ['Название пункта меню',  имя_функции ]
    ['Вывести весь справочник',print_phonebook],
    ['Найти абонента по фамилии',search_phonebook],
    ['Найти по номеру телефона', search_phonebook_by_phone],
    ['Добавить абонента в справочник', append_record_to_phonebook],
    ['Экспортировать файл в текстовом формате', export_to_txt],
    ['TODO: добавить функционал', lambda: None],
    ['Выход', lambda: None]
    ]




def print_main_menu():
    print()
    print(str("-" * 20))
    for i in range(len(main_menu_items)):
        print(f'[{i}] {main_menu_items[i][0]}')
    print(str("-" * 20))
    return int(input('Введите номер пункта меню: '))



choice = print_main_menu()
while (choice != len(main_menu_items) - 1):
    main_menu_items[choice][1]()
    choice = print_main_menu()

