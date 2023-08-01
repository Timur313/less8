import random

def start_victorina():
    day_list = ['первое', 'второе', 'третье', 'четвёртое',
        'пятое', 'шестое', 'седьмое', 'восьмое',
        'девятое', 'десятое', 'одиннадцатое', 'двенадцатое',
        'тринадцатое', 'четырнадцатое', 'пятнадцатое', 'шестнадцатое',
        'семнадцатое', 'восемнадцатое', 'девятнадцатое', 'двадцатое',
        'двадцать первое', 'двадцать второе', 'двадцать третье',
        'двадацать четвёртое', 'двадцать пятое', 'двадцать шестое',
        'двадцать седьмое', 'двадцать восьмое', 'двадцать девятое',
        'тридцатое', 'тридцать первое']
    month_list = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня',
           'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']

    famous_people = [
        {"name": "Блок Александр Александрович", "date_born": "16.11.1880"},
        {"name": "Высоцкий Владимир Семёнович",  "date_born": "25.01.1938"},
        {"name": "Грибоедов Александр Сергеевич", "date_born": "04.01.1795"},
        {"name": "Маяковский Владимир Владимирович", "date_born": "07.07.1893"},
        {"name": "Толстой Лев Николаевич", "date_born": "28.08.1828"},
        {"name": "Тургенев Иван Сергеевич", "date_born": "28.10.1818"},
        {"name": "Цветаева Марина Ивановна", "date_born": "08.10.1892"},
        {"name": "Чехов Антон Павлович", "date_born": "17.01.1860"},
        {"name": "Тютчев Федор Иванович", "date_born": "23.11.1803"},
        {"name": "Солженицын Александр Исаевич", "date_born": "11.12.1918"}
        ]

    rnd_ind = random.sample(range(0, 10), 5)

    restart = True
    while restart:
        print("Старт викторины!")
        print("Нужно угадать дату рождения известных людей")
        true_res = 0
        for ind_fp in rnd_ind:
            fam_peop = famous_people[ind_fp]
            fam_name = fam_peop["name"]
            real_date_born = fam_peop["date_born"]
            date_born = input(f"Введите дату рождения {fam_name} в формате \'dd.mm.yyyy\': ")

            if date_born == real_date_born:
                true_res += 1
                print("Верно!")
            else:
                mydate_split = [int(v) for v in real_date_born.split(".")]
                date_rem = f"{day_list[mydate_split[0]-1]} {month_list[mydate_split[1]-1]} {mydate_split[2]} году"
                print(f"Не верно! {fam_name} родился {date_rem}")

        print("Викторина завершена!")
        print("Статистика ответов:")
        print(f"Верно - {true_res} ({round(true_res / len(famous_people) * 100, 1)}%)")
        false_res = len(famous_people) - true_res
        print(f"Не Верно - {false_res} ({round(false_res / len(famous_people) * 100, 1)}%)")

        if false_res == 0:
            rest_val = input(f"Вы все угадали! Хотите попробовать еще раз? (введите - да)")
        else:
            rest_val = input(f"Попробуем еще раз? (введите - да)")

        if rest_val.lower() in ["da", "да"]:
            restart = True
        else:
            restart = False


