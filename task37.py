def number_filter():
    my_list = []
    for i in range(5):
        my_list.append(input('Введите значения: '))
    my_list.sort()
    return my_list[0], my_list[1]


print(number_filter())
