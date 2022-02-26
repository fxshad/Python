import os
from shutil import copy2


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
folder = os.path.join(BASE_DIR, 'my_project')



for dirpath, dirnames, filenames in os.walk(folder):
    # перебрать каталоги
    for dirname in dirnames:
        if dirname == 'templates':
            add_nested = os.listdir(os.path.join(dirpath, dirname))[0]
            list_files = os.listdir(os.path.join(dirpath, 'templates', add_nested))
            for i in list_files:
                # начальные пути файлов
                from_path = os.path.join(os.path.join(dirpath, 'templates', add_nested), i)
                if not os.path.exists(os.path.join(folder, 'templates', add_nested)):
                    os.makedirs(os.path.join(folder, 'templates', add_nested))
                    for n in list_files:
                        # конечные пути копируемых файлов
                        where_path = os.path.join(os.path.join(folder, 'templates', add_nested), n)
                        copy2(from_path, where_path)




