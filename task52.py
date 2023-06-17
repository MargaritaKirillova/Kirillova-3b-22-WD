my_list_1 = [1, 2, 3, 2, 1]
my_list_2 = my_list_1.copy()
my_list_2.reverse()
if my_list_1 == my_list_2:
    print('Массив является палиндромом')
else:
    print('Массив не является палиндромом')