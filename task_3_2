def num_translate_adv(value: str) -> str:
    """переводит числительное с английского на русский """
    # реализуйте здесь, где хранить необходимые исходные данные определитесь самостоятельно
    if value.lower() in num_lib:
        if value.istitle():
            str_out = num_lib.get(value.lower())
            str_out = str_out.title()
        else:
            str_out = num_lib.get(value)
    else:
        str_out = None
    str_out = str_out  #"в этой переменной должен оказаться результат перевода"
    return str_out


num_lib = {   'zero': 'ноль',  'one' : 'один',   'two' : 'два', 'three': 'три', 'four': 'четыре', 'five':'пять', 'six':'шесть', 'seven':'семь', 'eight': 'восемь', 'nine': 'девять', 'ten':'десять'
}

print(num_translate_adv("one"))
print(num_translate_adv("eight"))

print(num_translate_adv("Ten"))
print(num_translate_adv("Five"))
print(num_translate_adv("thirteen"))
print(num_translate_adv("Sixteen"))

print('\n\nEnd')

