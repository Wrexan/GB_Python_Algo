# -----------------------------------------------------------------------------
#                                   Задача
# 7.2 Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.

# -----------------------------------------------------------------------------
# Для сравнения присутствует алгоритм чет-нечет из предыдущего задания.
# При длине списка 5000 функция слияния выдает результат в 20 - 30 раз быстрее.
# -----------------------------------------------------------------------------
#                                  Реализация
import random
import cProfile

ra_limin = 0
ra_limax = 50
ra_size = 5_000


# -----------------------------------------------------------------------------
#                                    Randomizer
def rnd(size, limit_1, limit_2):
    ra = []
    for i in range(size):
        ra.append(random.randint(limit_1, limit_2))
    return ra


# -----------------------------------------------------------------------------
#                                    Вариант 1
def merge_sort(array):
    if len(array) <= 1:
        return
    left, right = array[:len(array) // 2], array[len(array) // 2:]
    merge_sort(left)
    merge_sort(right)
    n = m = k = 0
    center = [0] * (len(left) + len(right))
    while n < len(left) and m < len(right):
        if left[n] <= right[m]:
            center[k] = left[n]
            n += 1
        else:
            center[k] = right[m]
            m += 1
        k += 1
    while n < len(left):
        center[k] = left[n]
        n += 1
        k += 1
    while m < len(right):
        center[k] = right[m]
        m += 1
        k += 1
    for i in range(len(array)):
        array[i] = center[i]
    return array


# -----------------------------------------------------------------------------
#                                     Вариант 2
def bubble_sort_odd_even(array):
    done = False
    m = len(array) - 1
    n = m - 1
    while not done:
        done = True
        for i in range(0, m, 2):
            j = i + 1
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
                done = False
        for i in range(1, n, 2):
            j = i + 1
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
                done = False
    return array


# -----------------------------------------------------------------------------
#                                      main func
def main():
    ra_1 = rnd(ra_size, ra_limin, ra_limax)
    ra_2 = rnd(ra_size, ra_limin, ra_limax)
    print(merge_sort(ra_1))
    print(bubble_sort_odd_even(ra_2))


# -----------------------------------------------------------------------------
#


cProfile.run('main()')
