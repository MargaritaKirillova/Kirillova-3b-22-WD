print ('Введите первое число:')
a = input()
print('Введите второе число:')
b = input()
print('Введите операцию (=/-/*/%) :')
c = input()

if c == '+':
    print('Результат:', int(a) + int(b))
elif c == '-':
    print('Результат:', int(a) - int(b))
elif c == '*':
    print('Результат:', int(a) * int(b))
elif c == '%':
    print('Результат:', int(a) / int(b))
else:
    print('Я не знаю такую операцию')