import random
my_list = []
for n in range(15):
    my_list.append(random.randint(1, 50))
print(my_list)
print('Чётные числа из списка:')
for n in range(15):
    if my_list[n] % 2 == 0:
        print(my_list[n])
