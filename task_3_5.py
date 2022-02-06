import random


nouns = ["автомобиль", "лес", "огонь", "город", "дом", "кофе", "диван", "мост", "гит", "пароль", "салют"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью", "никогда", "постепенно", "сильно" ,"мега", "зачем-то", "практически", "аналогично", "абсолютно", "серьезно", "критически", "необдуманно"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий", "печальный", "быстрый", "красный", "тусклый", "отстойный", "гранитный", "медленный", "зачетный", "трудный", "грандиозный", "системный", "пугливый", "спорный", "задорный", "казуальный", "строптивый"]


def get_jokes(count: int) -> list:
    """Возвращает список шуток в количестве count"""
    # пишите реализацию своей программы здесь
    list_out = []
    for i in range(count):
        jok_str = ''
        jok_word = random.choice(nouns)
        jok_str += jok_word + ' '
        jok_word = random.choice(adverbs)
        jok_str += jok_word + ' '
        jok_word = random.choice(adjectives)
        jok_str += jok_word
        list_out.append(jok_str)

    list_out = list_out  #["здесь собранные шутки"]
    return list_out


print(get_jokes(2))
print(get_jokes(10))


print("\n")
def get_jokes_adv(count) -> list:
    """Return list count of jokes No repeat words """
     # пишите реализацию здесь
    list_out = []
    if count > min(len(nouns), len(adverbs), len(adjectives)):
        count = min(len(nouns), len(adverbs), len(adjectives))
    if count < 1:
        count = 0
    idx = 1
    list_out.extend(random.sample(nouns, k=count, counts=None))
    for adv in random.sample(adverbs, k=count, counts=None):
        list_out.insert(idx, adv)
        idx += 2
    idx = 2
    for adj in random.sample(adjectives, k=count, counts=None):
        list_out.insert(idx, adj)
        idx += 3
        _ = 0
    for i in range(0, len(list_out)):
        new_str = ''+' '.join(list(map(str, list_out[_:_+3])))
        _ += 4
        list_out.insert (i, new_str)
    list_out = list_out[0:count]
    return list_out


print(get_jokes_adv(66))


print('\n\nEnd')

