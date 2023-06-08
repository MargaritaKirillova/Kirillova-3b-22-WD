my_list = input('Введите слово на русском языке:')
vowels_list = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я',
               'А', 'Е', 'Ё', 'И', 'О', 'У', 'Ы', 'Э', 'Ю', 'Я']
vowels_count = 0
consonants_list = ['б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л',
                   'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ',
                   'Б', 'В', 'Г', 'Д', 'Ж', 'З', 'Й', 'К', 'Л',
                   'М', 'Н', 'П', 'Р', 'С', 'Т', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ']
consonants_count = 0

for i in my_list:
    if i in vowels_list:
        vowels_count += 1

    if i in consonants_list:
        consonants_count += 1

print('Количество гласных букв:', vowels_count)
print('Количество согласных букв:', consonants_count)
