# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

import random

ra_biggest_digit = 20
ra_size = 10
random_array = []
for i in range(ra_size):
    random_array.append(random.randint(0, ra_biggest_digit))

# Вариант 1
# n_min1 = random_array[1]
# n_min2 = random_array[0]
# for i in range(2, len(random_array)):
#     if n_min1 >= random_array[i]:
#         if n_min2 > n_min1:
#             n_min2 = n_min1
#         n_min1 = random_array[i]
#     elif n_min2 > random_array[i]:
#         n_min2 = random_array[i]

# Вариант 2
# n_min1 = min(random_array)
# n_min1_pos = random_array.index(n_min1)
# print([*random_array[:n_min1_pos], *random_array[n_min1_pos + 1:]])
# n_min2 = min([*random_array[:n_min1_pos], *random_array[n_min1_pos + 1:]])

# Вариант 3
n_min1 = min(random_array)
n_min1_pos = random_array.index(n_min1)
print(min(sorted(random_array[:n_min1_pos] + random_array[n_min1_pos + 1:])))
n_min2 = min(sorted(random_array[:n_min1_pos] + random_array[n_min1_pos + 1:]))

ra_sum = sum(random_array)
print(f'Два самых минимальных числа в массиве: {n_min1}, {n_min2}. Сам массив: \n{random_array}')
