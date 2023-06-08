print('Введите строку:')
a = input()


def reverse(word):
    my_list = []
    for i in range(len(word)-1, -1, -1):
        my_list += word[i]
    return my_list


print(reverse(a))