import os
try:
    a = int(input('Введите число: '))
    result = a*a
    print(result)
except ValueError:
    print('Ошибка')
finally:
    print('Завершение программы')
