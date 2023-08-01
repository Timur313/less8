import json
import os

def str2float(val: str):
    '''
    приводим к типу float
    '''
    try:
        res = float(str(val).replace(",", "."))
        if res < 0:
            print("Вы ввели не верное значение! Число должно быть положительным!")
            res = None
    except:
        print("Вы ввели не верное значение")
        res = None
    return res

def add_cash(full_cash, inp_v = None):
    if inp_v is None:
        inp_v = input('Введите сумму пополнения счета: ')
    cash_val = str2float(inp_v)
    if cash_val is None:
        dlt = 0
    else:
        dlt = cash_val
        print(f"Сумма добавлена. Баланс = {full_cash + dlt}")
    return full_cash + dlt

def buy_obj(hist: list, full_cash: float):
    inp_v = input('Введите сумму покупки: ')
    buy_val = str2float(inp_v)

    if buy_val is None:
        return hist, full_cash

    if buy_val > full_cash:
        print("К сожалению, денег не хватает")
        return hist, full_cash

    inp_v = input('Введите название покупки: ')
    hist.append({"name": inp_v, "summa": buy_val})
    full_cash -= buy_val
    return hist, full_cash

def print_buylist(hist_list):
    [print(v) for v in reversed(hist_list)]


def start_bank(CASH_FILENAME="cash.json", BUYLIST_FILENAME="buylist.json"):

    if not CASH_FILENAME in os.listdir():
        save_cash(CASH_FILENAME)
    if not BUYLIST_FILENAME in os.listdir():
        save_buylist(BUYLIST_FILENAME)

    full_cash = load_json(CASH_FILENAME)
    full_cash = float(full_cash["full_cash"])
    hist_list = load_json(BUYLIST_FILENAME)["buylist"]
    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        choice = input('Выберите пункт меню: ')
        if choice == '1':
            full_cash = add_cash(full_cash)
            save_cash(CASH_FILENAME, full_cash)
        elif choice == '2':
            hist_list, full_cash = buy_obj(hist_list, full_cash)
            save_cash(CASH_FILENAME, full_cash)
            save_buylist(BUYLIST_FILENAME, hist_list)
        elif choice == '3':
            print_buylist(hist_list)
        elif choice == '4':
            break
        else:
            print('Неверный пункт меню')

def load_json(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    return data

def save_cash(filename, full_cash=0):
    with open(filename, 'w') as f:
        json.dump({"full_cash": full_cash}, f)

def save_buylist(filename, buylist=[]):
    with open(filename, 'w') as f:
        json.dump({"buylist": buylist}, f)


if __name__ == '__main__':
    CASH_FILENAME = "cash.json"
    BUYLIST_FILENAME = "buylist.json"

    start_bank(CASH_FILENAME, BUYLIST_FILENAME)

