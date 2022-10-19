def show_menu():
    print('1 - Показать все')
    print('2 - Добавить запись')
    print('3 - Удалить запись')
    print('4 - Обновление')
    print('5 - Импорт в главный файл')
    print('6 - Экспорт в главный файл')
    return input('Введите цифру: ')


def inp():
    a = int(input('Введите индекс для изменения '))
    b = input('Введите новый номер телефона ')
    return a, b

def show_res(res):
    for i,row in enumerate(res):
        print(i,' '.join(row))

def add_csv():
    return input('Введите имя и телефон через пробел ')

def del_csv():
    return input('Введите индекс удаления ')