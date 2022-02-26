import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print(f'Корневая директория нашего проекта - {BASE_DIR}')
folder = os.path.join(BASE_DIR, 'my_project')
list_project = ['settings','mainapp','adminapp','authapp']
print(folder)
if not os.path.exists(folder):
    os.mkdir(folder)
    for i in list_project:
        i = os.path.join(folder, i)
        os.mkdir(i)

