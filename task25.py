n = int(input('Введите число: '))
counter = 0

for i in range(1, n+1):
     if n%i == 0:
         counter += 1
if counter == 2:
    print('Число простое')
else:
    print('Число составное')