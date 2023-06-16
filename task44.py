try:
    file = open('test.txt', 'r')
except FileNotFoundError:
    print('Файл не найден')
else:
    text = file.read()
    print(text)
    file.close()