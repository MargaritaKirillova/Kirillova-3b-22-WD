import random

array = [random.randint(1, 20) for i in range(20)]

a = int(input('Введите число: '))

if a in array:
    print('Число найдено в массиве')
else:
    print('Число не найдено в массиве')