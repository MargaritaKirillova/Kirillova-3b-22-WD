my_list = [5, 7, 11, 13, 15, 20, 25]
new_my_list = []

for i in range(len(my_list)):
    if my_list[i]>10:
        new_my_list.append(my_list[i])
sum_list = sum(new_my_list)
list_avg = sum_list/len(new_my_list)
print('Среднее арифметическое = ', list_avg)
