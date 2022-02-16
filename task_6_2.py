import task_6_1



list_out = list()
with open('nginx_logs.txt', 'r', encoding='utf-8') as fr:
    for line in fr.readlines():# передавайте данные в функцию и наполняйте список list_out кортежами
        line = task_6_1.get_parse_attrs(line)
        list_out.append(line[0])



print('ip спамера и кол-во запросов') #если не ошибся))
freg_dict = {}
for i in list_out:
    freg_dict.setdefault(i, 0)
for i in list_out:
    freg_dict[i] = freg_dict.get(i) + 1
for i in freg_dict:
    if freg_dict.get(i) == max(freg_dict.values()):
        print(i, '>>>>>>', freg_dict[i])
        break
print('\n\nEnd')
