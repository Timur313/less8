from actions import *
from victorina import start_victorina
from bank import start_bank

if __name__ == '__main__':
    my_event = {
        "1" : {"text": "создать папку",
               "func": create_folder},
        "2" : {"text": "удалить (файл/папку)",
               "func": delete_object},
        "3" : {"text": "копировать (файл/папку)",
               "func": copy_folder},
        "4" : {"text": "просмотр содержимого рабочей директории",
               "func": print_folder_contents},
        "5" : {"text": "посмотреть только папки",
               "func": print_folder_contents_only_folder},
        "6" : {"text": "посмотреть только файлы",
               "func": print_folder_contents_only_files},
        "7" : {"text": "просмотр информации об операционной системе",
               "func": print_platform},
        "8" : {"text": "создатель программы",
               "func": print_author},
        "9" : {"text": "играть в викторину",
               "func": start_victorina},
        "10": {"text": "мой банковский счет",
               "func": start_bank},
        "11": {"text": "сохранить содержимое рабочей директории в файл",
               "func": export2file},
        "12": {"text": "выход",
               "func": None}
    }
    print("Консольный файловый менеджер запущен")
    while True:
        for idv, val in my_event.items():
            text = val["text"]
            print(f"{idv} - {text}")

        choice = input('Выберите пункт меню: ')
        if choice == "12":
            break
        choice_val = my_event.get(choice)
        if not choice_val is None:
            choice_val['func']()
        else:
            print('Неверный пункт меню')
