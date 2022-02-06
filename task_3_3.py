def thesaurus(*args) -> dict:
    # пишите свою реализацию здесь
    global dict_for_global             # исключительно для вывода словаря в вертикальном формате!!!
    dict_out = {}
    name_list = list(args)             # создать список входящих имен
    name_list.sort()
    for i in name_list:
        dict_out.setdefault(i[0], [i]) # создать "каркас" словаря
    for i in dict_out:                 # взять ключ
        for n in name_list:            # взять имя из списка
            if n in dict_out[i]:       # есть ли имя в словаре?
                continue               # если нет, не добавит
            elif n[0] != i:            # ключ и первая буква имени совпадает?
                continue               # если нет, не добавит
            else:
                dict_out[i].append(n)  # добавить имя
    dict_for_global = dict_out
    dict_out = dict_out  # результирующий словарь значений
    return dict_out


print(thesaurus("Ярослав", "Иван", "Иван", "Иван", "Мария", "Петр", "Илья", "Алексей", "Владимир", "Виктор", "Варвара", "Вадим", "Анатолий", "Михаил", "Светлана", "Игорь", "Олег"))

for k, v in dict_for_global.items():
    print(k, v)

print('\n\nEnd')
