# Написать программу, которая принимает последовательность чисел и выводит на экран два числа: значение наибольшего элемента последовательности и порядковый номер этого элемента.
    
# задаём количество элементов в массиве
n = int(input('Введите, сколько чисел будет в массиве: '))

# создаём массив
my_list = []
for i in range(n):
    my_list.append(input('Введите число: '))
    
# создаём копию массива, для её отсортировки
copy = my_list.copy()
copy.sort()

# определяем наибольшее число в массиве
my_list_last = copy[-1]

# определяем порядковый номер наибольшего числа и выводим его вместе с самим числом
last_index = my_list.index(my_list_last)

print("Наибольшее число: ", my_list_last, ";", "Его порядковый номер: ", last_index)
