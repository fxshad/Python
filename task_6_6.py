import sys
from pprint import pprint


""" Usages:
    python task_6_6.py add_sale.py 
    python task_6_6.py show_sales.py
"""


with open('bakery.csv', 'a+', encoding='utf-8') as f:
    if sys.argv[1] == 'add_sale.py':
        num = sys.argv[2]
        if float(num):
            f.writelines(num + '\n')



def read_func():
    with open('bakery.csv', encoding='utf-8') as fr:
        show = fr.readlines()
    return show



if sys.argv[1] == 'show_sales.py' and len(sys.argv) == 4:
    begin = int(sys.argv[2]) - 1
    end = int(sys.argv[3])
    for i in range(begin, end):
        pprint(read_func()[i].rstrip())
elif len(sys.argv) == 3 and sys.argv[1] == 'show_sales.py':
    begin = int(sys.argv[2]) - 1
    for i in range(begin, len(read_func())):
        pprint(read_func()[i].rstrip())
else:
    if sys.argv[1] == 'show_sales.py':
        for i in read_func():
            pprint(i.rstrip())

# Подумать, как избежать чтения всего файла при реализации второго и третьего случаев.
"""вероятно с помощью chunk"""


