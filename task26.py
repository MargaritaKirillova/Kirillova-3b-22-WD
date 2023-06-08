print('Введите первое число')
a = input()
print('Введите второе число')
b = input()
for n in range(2, int(min(a,b))):
    if (int(a)%n==0) and (int(b)%n==0):
        print('Наименьший общий множитель равен:', n)
        exit()
print('Наименьший общий множитель равен: 1')