import requests


def currency_rates(code: str) -> float:
    """возвращает курс валюты `code` по отношению к рублю"""
    # ваша реализация здесь
    response = requests.get("http://www.cbr.ru/scripts/XML_daily.asp")
    idx = 0
    if code.islower():
        code = code.upper()
    r = response.text
    result_value = 0
    if code not in r or len(code) <3:
        result_value = None
    else:
        pars_list = r.split('/')
        for i in pars_list:
            if code in i:
                idx = (pars_list.index(i))
                idx += 3
        str_nom = pars_list[idx - 2]
        str_value = pars_list[idx]
        result_value = ''
        nom = ''
        for i in str_nom:
            if i.isdigit():
                nom += i
        for i in str_value:
            if i.isdigit():
                result_value += i
        nom = int(nom)
        result_value =  round((float(result_value) / 10000)/nom, 4) ## здесь должно оказаться результирующее значение float
    return result_value


if __name__ == '__main__':
    print('"')