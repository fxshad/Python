import re


def email_parse(email: str) -> dict:
    """
    Парсит переданную email-строку на атрибуты и возвращает словарь
    :param email: строковое входное значение обрабатываемого email
    :return: {'username': <значение до символа @>, 'domain': <значение за символом @>} | ValueError
    """
    RE_MAIL = re.compile(r'[a-zA-Z0-9]+')
    if not re.search('\.',email):
        raise ValueError(f'wrong email: {email}')
    if re.search('[^a-zA-Z0-9@\.]', email):
        raise ValueError(f'wrong email: {email}')
    return {'username': RE_MAIL.findall(email)[0], 'domain': RE_MAIL.findall(email)[1]}




if __name__ == '__main__':
    email_parse('someone@geekbrains.ru')
    email_parse('someone@geekbrainsru')




