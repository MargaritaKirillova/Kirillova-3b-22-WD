try:
    a = int(input('Введите первое число: '))
    b = int(input('Введите второе число: '))
    result = a / b
    print(f'Результат: {result}')
except ValueError:
    print('Неверный формат числа')
except ZeroDivisionError:
    print('Деление на ноль невозможно')
except Exception as e:
    print('Произошла ошибка: {e}')
finally:
    print('Завершение программы')