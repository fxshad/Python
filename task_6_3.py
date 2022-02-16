import sys
import json


def prepare_dataset(path_users_file: str, path_hobby_file: str) -> dict:
    """
    Считывает данные из файлов и возвращает словарь, где:
        ключ — ФИО, значение — данные о хобби (список строковых переменных)
    :param path_users_file: путь до файла, содержащий ФИО пользователей, разделенных запятой по строке
    :param path_hobby_file: путь до файла, содержащий хобби, разделенные запятой по строке
    :return: Dict(str: Union[List[str]|None])
    """
    # Ваш код пишите здесь
    some_dict = {}

    with open('users.csv', encoding='utf-8') as f_users:
        with open('hobby.csv', encoding='utf-8') as f_hobby:
            l_hobby = f_hobby.readlines()
        l_usrs = f_users.readlines()
        if len(l_hobby) > len(l_usrs):
            sys.exit(1)
        for i in range(len(l_usrs)):
            key = l_usrs[i].split(",")
            key = " ".join(key)
            if i == len(l_hobby):
                val = None
            else:
                val = l_hobby[i].rstrip().split(',')
            some_dict.setdefault(key.rstrip(), val)



    return  some_dict# верните словарь, либо завершите исполнение программы кодом 1


dict_out = prepare_dataset('users.csv', 'hobby.csv')
with open('task_6_3_result.json', 'w', encoding='utf-8') as fw:
    json.dump(dict_out, fw, ensure_ascii=False, indent=2)


print('\n\n End')