# -----------------------------------------------------------------------------
#                                   Задача
# 4.1 Проанализировать скорость и сложность одного любого алгоритма,
# разработанных в рамках практического задания первых трех уроков.
# Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.

# 3.7 В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

# -----------------------------------------------------------------------------
#                                  Примечание
# За основу взято задание 3.7 с добавлением встроенной функции для сравнения.
# Тест с использованием timeit производился с разным размером и разбросом случайных переменных
# Размер списка 10, разброс 0-10
# 13.9964
# 14.2781
# 15.0714
# 13.6099
#
# Размер списка 100, разброс 0-100
# 122.4594
# 118.6156
# 127.2930
# 116.0235
#
# Размер списка 1000, разброс 0-1000
# 1303.6535
# 1246.9236
# 1371.5459
# 1182.8377
#
# Как видно из теста, время выполнения поиска слишком мало в сравнении с остальным кодом.
# При малом размере списка быстрее всего четвертый и первый варианты.
# При увеличении обьема входящих данных вперед вырывается четвертый и второй варианты.
# На ПК с более мощным процессором отрыв увеличивается, сильнее всего отстает 3й вариант (слияние списков через sorted).
#   К слову 3й вариант был найден в интернете как самый быстрый для слияния, однако распаковка оказалась быстрее.
# Сравнить же отдельно операции сложно из-за разной реализации и невозможности брать информацию из вне.

# -----------------------------------------------------------------------------
#                                  Реализация
# import random
import timeit

# ra_biggest_digit = 20
# ra_size = 10
# random_array = []
# for i in range(ra_size):
#     random_array.append(random.randint(0, ra_biggest_digit))

# -----------------------------------------------------------------------------
#                                    Вариант 1
# n_min1 = random_array[1]
# n_min2 = random_array[0]
# for i in range(2, len(random_array)):
#     if n_min1 >= random_array[i]:
#         if n_min2 > n_min1:
#             n_min2 = n_min1
#         n_min1 = random_array[i]
#     elif n_min2 > random_array[i]:
#         n_min2 = random_array[i]

print(timeit.timeit("""
import random
ra_biggest_digit = 10
ra_size = 10
random_array = []
for i in range(ra_size):
    random_array.append(random.randint(0, ra_biggest_digit))

n_min1 = random_array[1]
n_min2 = random_array[0]
for i in range(2, len(random_array)):
    if n_min1 >= random_array[i]:
        if n_min2 > n_min1:
            n_min2 = n_min1
        n_min1 = random_array[i]
    elif n_min2 > random_array[i]:
        n_min2 = random_array[i]
"""))
# -----------------------------------------------------------------------------
#                                     Вариант 2
# n_min1 = min(random_array)
# n_min1_pos = random_array.index(n_min1)
# print([*random_array[:n_min1_pos], *random_array[n_min1_pos + 1:]])
# n_min2 = min([*random_array[:n_min1_pos], *random_array[n_min1_pos + 1:]])

print(timeit.timeit("""
import random
ra_biggest_digit = 10
ra_size = 10
random_array = []
for i in range(ra_size):
    random_array.append(random.randint(0, ra_biggest_digit))
    
n_min1 = min(random_array)
n_min1_pos = random_array.index(n_min1)
n_min2 = min([*random_array[:n_min1_pos], *random_array[n_min1_pos + 1:]])
"""))
# -----------------------------------------------------------------------------
#                                      Вариант 3
# n_min1 = min(random_array)
# n_min1_pos = random_array.index(n_min1)
# print(min(sorted(random_array[:n_min1_pos] + random_array[n_min1_pos + 1:])))
# n_min2 = min(sorted(random_array[:n_min1_pos] + random_array[n_min1_pos + 1:]))

print(timeit.timeit("""
import random
ra_biggest_digit = 10
ra_size = 10
random_array = []
for i in range(ra_size):
    random_array.append(random.randint(0, ra_biggest_digit))

n_min1 = min(random_array)
n_min1_pos = random_array.index(n_min1)
n_min2 = min(sorted(random_array[:n_min1_pos] + random_array[n_min1_pos + 1:]))
"""))

# -----------------------------------------------------------------------------
#                                      Вариант 4
# n_min1 = random_array.remove(min(random_array))
# n_min2 = random_array.remove(min(random_array))

print(timeit.timeit("""
import random
ra_biggest_digit = 10
ra_size = 10
random_array = []
for i in range(ra_size):
    random_array.append(random.randint(0, ra_biggest_digit))

n_min1 = random_array.remove(min(random_array))
n_min2 = random_array.remove(min(random_array))
"""))

# -----------------------------------------------------------------------------
#                                   Вывод результата
# ra_sum = sum(random_array)
# print(f'Два самых минимальных числа в массиве: {n_min1}, {n_min2}. Сам массив: \n{random_array}')
