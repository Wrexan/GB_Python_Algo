# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

import random

ra_biggest_digit = 100
ra_size = 20
random_array = []
for i in range(ra_size):
    r = random.randint(-ra_biggest_digit, ra_biggest_digit)
    random_array.append(r)

n = 0
p = 0
for i in range(len(random_array)):
    if random_array[i] < n:
        n = random_array[i]
        p = i

print(f'Минимальное число в массиве: {n}. Его позиция: {p}. Сам массив: \n{random_array}')
