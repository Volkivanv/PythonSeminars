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

def insert_person(filename, person):
    with open(filename, 'a', encoding='utf-8') as f_obj:
        f_obj.write(f"{person}\n")


def print_file(filename):
    with open(filename, 'r', encoding='utf-8') as f_obj:
        content = f_obj.read()
        print(content)


def seek_in_file(filename, keyword):
    with open(filename, 'r', encoding='utf-8') as f_obj:
        for line in f_obj:
            lst = line.split()
            if keyword in lst:
                print(line)


command = input("Введите команду: Новая запись - new, вывод списка - list, найти - seek, выход - exit: ")
while command != 'exit':
    if command == 'new':
        insert_person('guid.txt', input("Введите Фамилию Имя Отчество и телефон через пробел: "))
    if command == 'list':
        print_file('guid.txt')
    if command == 'seek':
        seek_in_file('guid.txt',input("Введите ключевое слово: "))
    command = input("Введите команду: Новая запись в справочке - new, выход - exit: ")
