def get_uniq_numbers(src: list):
    new_list = [i for i in src if src.count(i) == 1]
    return new_list


src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(*get_uniq_numbers(src))
print(get_uniq_numbers(src))

print("\n\nEnd")