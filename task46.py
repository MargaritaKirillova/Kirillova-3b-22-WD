try:
    file = open('test.txt', 'w')
    file.write('Hello, world!')
except FileNotFoundError:
    print('Ошибка')
except IOError:
    print('Ошибка')
