# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random
ra_biggest_digit = 100
ra_size = 20
random_array = []
for i in range(ra_size):
    r = random.randint(0, ra_biggest_digit)
    while r in random_array:
        r = random.randint(0, ra_biggest_digit)
    random_array.append(r)
mn, mx = min(random_array), max(random_array)
mn_pos, mx_pos = random_array.index(mn), random_array.index(mx)
print(f'Массив случайных чисел до и после заменя местами минимума и максимума {mn}, {mx}: \n{random_array}')
random_array[mx_pos], random_array[mn_pos] = mn, mx

print(f'{random_array}')
