# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Самый минимальный и максимальный элементы в сумму не включать.

import random

ra_biggest_digit = 70
ra_size = 50
random_array = []
for i in range(ra_size):
    random_array.append(random.randint(0, ra_biggest_digit))

n_min = [random_array[0], 0]
n_max = [random_array[0], 0]
for i in range(len(random_array)):
    # print(f'{i = }  {random_array[i] = }  {n_min = }  {n_max = }')
    if n_min[0] > random_array[i]:
        n_min[0], n_min[1] = random_array[i], 1
        # print(f'if {n_min = }')
    elif n_min[0] == random_array[i]:
        n_min[1] += 1
        # print(f'elif {n_min = }')
    if n_max[0] < random_array[i]:
        n_max[0], n_max[1] = random_array[i], 1
        # print(f'if {n_max = }')
    elif n_max[0] == random_array[i]:
        n_max[1] += 1
        # print(f'elif {n_max = }')
ra_sum = sum(random_array)
print(f'Минимальное число в массиве: {n_min[0]} ({n_min[1]}шт), максимальное: {n_max[0]} ({n_max[1]}шт),\n'
      f'сумма элементов массива {ra_sum}, а сумма без их учета: {ra_sum - n_max[0] * n_max[1] - n_min[0] * n_min[1]}'
      f' Сам массив: \n{random_array}')
