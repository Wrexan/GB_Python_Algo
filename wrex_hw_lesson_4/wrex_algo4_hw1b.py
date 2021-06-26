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
# Размер списка 1_000_000, разброс 0-10_000_000
#
#     ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.094    0.094    0.094    0.094 wrex_algo4_hw1b.py:56(two_mins_cycle)
#         1    0.019    0.019    0.055    0.055 wrex_algo4_hw1b.py:71(two_mins_min_repack)
#         1    0.033    0.033    0.359    0.359 wrex_algo4_hw1b.py:80(two_mins_min_sorted)
#         1    0.000    0.000    0.039    0.039 wrex_algo4_hw1b.py:89(two_mins_min_remove)
#         1    0.000    0.000    0.548    0.548 wrex_algo4_hw1b.py:97(main)
#
#
# Размер списка 10_000_000, разброс 0-10_000_000
#
#     ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.829    0.829    0.829    0.829 wrex_algo4_hw1b.py:54(two_mins_cycle)
#         1    0.199    0.199    0.517    0.517 wrex_algo4_hw1b.py:69(two_mins_min_repack)
#         1    0.424    0.424    4.963    4.963 wrex_algo4_hw1b.py:78(two_mins_min_sorted)
#         1    0.000    0.000    0.395    0.395 wrex_algo4_hw1b.py:87(two_mins_min_remove)
#         1    0.000    0.000    6.704    6.704 wrex_algo4_hw1b.py:95(main)
#
# Размер списка 100_000_000, разброс 0-10_000_000
#
#     ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    7.355    7.355    7.355    7.355 wrex_algo4_hw1b.py:58(two_mins_cycle)
#         1    1.860    1.860    4.085    4.085 wrex_algo4_hw1b.py:73(two_mins_min_repack)
#         1    5.057    5.057   66.274   66.274 wrex_algo4_hw1b.py:82(two_mins_min_sorted)
#         1    0.000    0.000    2.582    2.582 wrex_algo4_hw1b.py:91(two_mins_min_remove)
#         1    0.000    0.000   80.296   80.296 wrex_algo4_hw1b.py:99(main)

# 100
#
#
#                                                                   sor
#
#
#
#                                                   sor
#
#
#
# 10
#
#
#                                                                   cyc
#
#
#                                  sor
#                                                   cyc             rep
#
#                                                                   rem
#                  sor                              rep
#                                                   rem
# 1
#
#                                  cyc
#
#
#
#                  cyc             rep
#   sor
#                                  rem
#   cyc            rep
#   rep            rem
#   rem
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# 1_000_000                     10_000_000                     100_000_000

# Как показывают результаты теста, для большого количества рассчетов вариант 3 (с объединением списков через sorted)
# не подходит совершенно, на 100 миллионах операций он оказался месленнее встроенных методов в 25 раз.
# Самым быстрым ожидаемо остался встроенный метод в варианте 4, метод распаковки медленнее примерно в 2 раза,
# а перебор в 4 раза.
# Если учесть тот факт, что в вариантах 2 и 3 операция со списками производится всего один раз, в 4 вырианте
# для каждой переменной, а 1й вариант производит только цикл с выборкой, усложнение задачи(например выборка 3 или 10
# минимумов) может увеличить разрыв в скорости исполнения алгоритмов еще в несколько раз.

# -----------------------------------------------------------------------------
#                                  Реализация
import random
import cProfile

ra_biggest_digit = 10_000_000
ra_size = 5_000_000
random_array = []
for i in range(ra_size):
    random_array.append(random.randint(0, ra_biggest_digit))


# -----------------------------------------------------------------------------
#                                    Вариант 1
def two_mins_cycle(ra):
    n_min1 = ra[1]
    n_min2 = ra[0]
    for i in range(2, len(ra)):
        if n_min1 >= ra[i]:
            if n_min2 > n_min1:
                n_min2 = n_min1
            n_min1 = ra[i]
        elif n_min2 > ra[i]:
            n_min2 = ra[i]
    return n_min1, n_min2


# -----------------------------------------------------------------------------
#                                     Вариант 2
def two_mins_min_repack(ra):
    n_min1 = min(ra)
    n_min1_pos = ra.index(n_min1)
    n_min2 = min([*ra[:n_min1_pos], *ra[n_min1_pos + 1:]])
    return n_min1, n_min2


# -----------------------------------------------------------------------------
#                                      Вариант 3
def two_mins_min_sorted(ra):
    n_min1 = min(ra)
    n_min1_pos = ra.index(n_min1)
    n_min2 = min(sorted(ra[:n_min1_pos] + ra[n_min1_pos + 1:]))
    return n_min1, n_min2


# -----------------------------------------------------------------------------
#                                      Вариант 4
def two_mins_min_remove(ra):
    n_min1 = ra.remove(min(ra))
    n_min2 = ra.remove(min(ra))
    return n_min1, n_min2


# -----------------------------------------------------------------------------
#                                      main func
def main():
    two_mins_cycle(random_array)
    two_mins_min_repack(random_array)
    two_mins_min_sorted(random_array)
    two_mins_min_remove(random_array)


# -----------------------------------------------------------------------------
#                                   Вывод результата
# ra_sum = sum(random_array)
# print(f'Два самых минимальных числа в массиве: {n_min1}, {n_min2}. Сам массив: \n{random_array}')

cProfile.run('main()')
