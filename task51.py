from functools import reduce
from math import gcd

my_list_1 = [24, 36, 48, 60]
my_list_2 = [12, 18, 24, 36, 72]
my_list_1.extend(my_list_2)
result = reduce(gcd, my_list_1)
print('Наибольший общий делитель = ', result)
