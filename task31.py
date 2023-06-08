from calculator import addition, subtraction, multiplication, division


n = input('Введите операцию (+/-/*/%) :')

if n in ('+', '-', '*', '%'):
    a = (input('Введите значение a:'))
    b = (input('Введите значение b:'))

    if n == "+":
        print(addition(a, b))

    if n == "-":
        print(subtraction(a, b))

    if n == "*":
        print(multiplication(a, b))

    if n == "%":
        print(division(a, b))


else:
    print('Я не знаю эту операцию')