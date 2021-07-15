# -----------------------------------------------------------------------------
#                                   Задача
# 7.2 Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой – не больше медианы.
# Задачу можно решить без сортировки исходного массива.
# Но если это слишком сложно, то используйте метод сортировки, который не рассматривался на уроках
# -----------------------------------------------------------------------------
# Для сравнения присутствует алгоритм чет-нечет из предыдущего задания.
# При длине списка 5000 функция слияния выдает результат в 20 - 30 раз быстрее.
# -----------------------------------------------------------------------------
#                                     Данные
import random
# import cProfile

ra_limin = 0
ra_limax = 100
ra_size = 2 * 100 + 1


# -----------------------------------------------------------------------------
#                                    Randomizer
def rnd(size, limit_1, limit_2):
    ra = []
    for i in range(size):
        ra.append(random.randint(limit_1, limit_2))
    return ra


# -----------------------------------------------------------------------------
#                                    Поиск медианы
def median_brute_search(array, delta_max):
    a_size = len(array)
    median = median_old = delta = 0
    for i in range(a_size):
        lower, higher = 0, 0
        for j in range(a_size):
            if array[j] != array[i]:
                if array[j] > array[i]:
                    higher += 1
                else:
                    lower += 1
        # print(f'{i=}    {lower=} {higher=}    {array[i]=}')
        delta = abs(lower - higher)
        if delta == 0:
            print('YAY')
            return array[i]
        else:
            if delta <= delta_max:
                median_old = median
                median = array[i]
                # if delta <= 1:
                #     # print(f'{delta=} {array[i]=} {median_h=}')
                #     # if abs(median - array[i]) <= 1:
                #     #     return median if median > array[i] else array[i]
                #     # else:
                #     median = (array[i])
                # else:
                #     median = array[i]
                delta_max = delta
                print(f'{delta=} {array[i]=}')
            if delta <= 3:
                print(f'{median=}  {array[i]=} {median_old=} {delta_max=}    {lower=} {higher=}')
    return median


# -----------------------------------------------------------------------------
#                                      main func
def main():
    ra_1 = rnd(ra_size, ra_limin, ra_limax)
    ra_2 = rnd(100, ra_limin, ra_limax)
    print(f'array 1 (201): {ra_1}')
    print(f'median: {median_brute_search(ra_1, ra_limax - ra_limin)}')
    print(f'array 2 (100): {ra_2}')
    print(f'median: {median_brute_search(ra_2, ra_limax - ra_limin)}')


# -----------------------------------------------------------------------------
#


# cProfile.run('main()')
main()
