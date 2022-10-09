import random

f = open(r'C:\Users\howie\Downloads\climate_id_00.txt', 'r', encoding='utf-8')

l = f.read().split("\n")

f = open(r'C:\Users\howie\Downloads\climate_id_01.txt', 'r', encoding='utf-8')

l += f.read().split("\n")

f = open(r'C:\Users\howie\Downloads\climate_id_02.txt', 'r', encoding='utf-8')

l += f.read().split("\n")

f = open(r'C:\Users\howie\Downloads\climate_id_03.txt', 'r', encoding='utf-8')

l += f.read().split("\n")

random.shuffle(l)

i = 0

with open("climate_id_1.txt", 'w', newline='') as f1, open("climate_id_2.txt", 'w', newline='') as f2:
    for id in l:
        if (i % 2 == 0):
            f1.write(id + "\n")
        else:
            f2.write(id + "\n")
        i += 1


