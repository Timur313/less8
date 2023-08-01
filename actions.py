import sys
import os
import shutil
from distutils.dir_util import copy_tree
from os.path import isfile, join

def create_folder():
    try:
        inp_val = input('Введите название папки: ')
        if not os.path.isdir(inp_val):
            os.mkdir(inp_val)
    except BaseException as e:
        print(f"Ошибка при создании папки: {e}")

def delete_object():
    try:
        inp_val = input('Введите название файла/папки: ')
        if "." in inp_val:
            os.remove(inp_val)
        else:
            shutil.rmtree(inp_val)
    except BaseException as e:
        print(f"Ошибка при удалении: {e}")

def copy_folder():
    try:
        old_val = input('Введите название копируемой папки: ')
        new_val = input('Введите название новой папки: ')
        copy_tree(old_val, new_val)
    except BaseException as e:
        print(f"Ошибка при копировании: {e}")

def try_except_decor(func):
    def inner(*args, **kwargs):
        res = None
        try:
            res = func(*args, **kwargs)
        except BaseException as e:
            print(f"Ошибка при выводе содержимого: {e}")
        return res
    return inner

@try_except_decor
def print_folder_contents():
    inp_val = input('Введите название папки: ')
    print(os.listdir(inp_val))

@try_except_decor
def print_folder_contents_only_folder():
    inp_val = input('Введите название папки: ')
    onlyfolder = get_folder_contents_only_folder(inp_val)
    print(onlyfolder)

@try_except_decor
def print_folder_contents_only_files():
    inp_val = input('Введите название папки: ')
    onlyfiles = get_folder_contents_only_files(inp_val)
    print(onlyfiles)

def get_folder_contents_only_folder(folder = "."):
    onlyfolder = []
    try:
        onlyfolder = [f for f in os.listdir(folder) if not isfile(join(folder, f))]
    except BaseException as e:
        print(f"Ошибка при выводе содержимого: {e}")
    return onlyfolder

def get_folder_contents_only_files(folder = "."):
    onlyfiles = []
    try:
        onlyfiles = [f for f in os.listdir(folder) if isfile(join(folder, f))]
    except BaseException as e:
        print(f"Ошибка при выводе содержимого: {e}")
    return onlyfiles

def print_platform():
    try:
        print(sys.platform)
    except BaseException as e:
        print(f"Ошибка при получении информации об ОС: {e}")

def print_author():
    print("Timur313")

def get_fold_and_file():
    cont_info = {
        "files": [],
        "dirs": []
    }
    cont_info["files"] = get_folder_contents_only_files()
    cont_info["dirs" ] = get_folder_contents_only_folder()
    return cont_info

def export2file(filename="listdir.txt"):
    cont_info = get_fold_and_file()
    with open(filename, 'w') as f:
        f.write(f"files: " + ",".join(cont_info["files"]) + "\n")
        f.write(f"dirs: "  + ",".join(cont_info["dirs" ]) + "\n")
