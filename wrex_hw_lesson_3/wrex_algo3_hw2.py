# 2. Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
# то во второй массив надо заполнить значениями 1, 4, 5, 6
# (или 0, 3, 4, 5 - если индексация начинается с нуля),
# т.к. именно в этих позициях первого массива стоят четные числа.

import random
ra_biggest_digit = 100
ra_size = 10
random_array = []
even_array = []
for i in range(ra_size):
    random_array.append(random.randint(0, ra_biggest_digit))
    if random_array[i] % 2 == 0:
        even_array.append(i)
print(f'Массив случайных чисел: {random_array}\nИндексы четных чисел (начиная с 0): {even_array}')
