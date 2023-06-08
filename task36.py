str1 = str(input('Введите первую строку: '))
str2 = str(input('Введите вторую строку: '))
my_list = []


def first_let (letter1, letter2):
    my_list.append(letter1[0].upper())
    my_list.append(letter2[0].upper())
    return my_list


print(first_let(str1, str2))
