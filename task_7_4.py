import os


dir = '' # путь до директории

size_10 = size_100 = size_1000 = size_10000 = size_100000 =  0
stat_dict = {10: size_10, 100: size_100, 1000: size_1000, 10000: size_10000, 100000: size_100000}
for root, dirs, files in os.walk(dir):
    for file in files:
        if os.stat(os.path.join(root,file)).st_size <= 10:
            size_10 += 1
            stat_dict[10] = size_10
        if os.stat(os.path.join(root,file)).st_size <= 100 and os.stat(os.path.join(root,file)).st_size > 10:
            size_100 += 1
            stat_dict[100] = size_100
        if os.stat(os.path.join(root,file)).st_size <= 1000 and os.stat(os.path.join(root,file)).st_size > 100:
            size_1000 += 1
            stat_dict[1000] = size_1000
        if os.stat(os.path.join(root,file)).st_size <= 10000 and os.stat(os.path.join(root,file)).st_size > 1000:
            size_10000 += 1
            stat_dict[10000] = size_10000
        if os.stat(os.path.join(root,file)).st_size <= 100000 and os.stat(os.path.join(root,file)).st_size > 10000:
            size_10000 += 1
            stat_dict[100000] = size_100000

print(stat_dict)

