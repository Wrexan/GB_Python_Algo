# 4. Определить, какое число в массиве встречается чаще всего.

import random

ra_biggest_digit = 10
ra_size = 20
random_array = []
for i in range(ra_size):
    r = random.randint(0, ra_biggest_digit)
    random_array.append(r)

temp_array = [random_array[0], 0]
for i in random_array:
    for t in range(0, (len(temp_array)), 2):
        if temp_array[t] == i:
            temp_array[t + 1] += 1
            break
    else:
        temp_array += i, 1

result_id = 0
for t in range(0, (len(temp_array)), 2):
    if temp_array[t + 1] > temp_array[result_id + 1]:
        result_id = t

print(f'Массив случайных чисел и самое часто встречающееся число: \n{random_array}\n'
      f'Число {temp_array[result_id]} встречается {temp_array[result_id+1]} раз(а)')
