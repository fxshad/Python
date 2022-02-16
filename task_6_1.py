from pprint import pprint


def get_parse_attrs(line: str) -> tuple:
    """Парсит строку на атрибуты и возвращает кортеж атрибутов (<remote_addr>, <request_type>, <requested_resource>)"""
    remote_addr = (line[:line.find(' ')])
    if 'GET' in line:
        request_type = (line[line.find('GET'):line.find('GET') + 3])
    else:
        request_type = (line[line.find('HEAD'):line.find('HEAD') + 4])
    requested_resource = (line[line.find('downloads') - 1:line.find('downloads') + 19])
    lo = (remote_addr, request_type, requested_resource)
    return  lo# верните кортеж значений <remote_addr>, <request_type>, <requested_resource>


if __name__ == '__main__':
    list_out = list()
    with open('nginx_logs.txt', 'r', encoding='utf-8') as fr:
        for line in fr.readlines():# передавайте данные в функцию и наполняйте список list_out кортежами
            line = get_parse_attrs(line)
            list_out.append(line)
    pprint(list_out)
    """добавил памяти для консоли по совету из чата, является ли это верным решением?"""
    print(f'\n\nEnd')