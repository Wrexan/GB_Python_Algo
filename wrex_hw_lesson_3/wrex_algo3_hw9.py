# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random


def rm(ra_size):
    ra_biggest_digit = 50
    ra = []
    for i in range(ra_size):
        ra.append(random.randint(0, ra_biggest_digit))
    return ra


mtrx_sizx = 15
mtrx_sizy = 15
mtrx = rm(mtrx_sizx * mtrx_sizy)
max_of_min = None

for x in range(mtrx_sizx):
    # print(f'{x=}', end='; ')
    y_min = None
    for y in range(mtrx_sizy):
        y_now = mtrx[x + y * mtrx_sizy]
        if y_min is None or y_min > y_now:
            y_min = y_now
        # print(f'{y=}; {y_now=}; {y_min=}')
    if max_of_min is None or max_of_min < y_min:
        max_of_min = y_min
    # print(f'{max_of_min=}')

# По ошибке написал для минимумов в строке
# for y in range(mtrx_sizy):
#     print(f'{y=}', end='; ')
#     x_min = None
#     for x in range(mtrx_sizx):
#         x_now = mtrx[x + y * mtrx_sizx]
#         if x_min is None or x_min > x_now:
#             x_min = x_now
#         print(f'{x=}; {x_now=}; {x_min=}')
#     if max_of_min is None or max_of_min < x_min:
#         max_of_min = x_min
#     print(f'{max_of_min=}')

for i in range(len(mtrx)):
    print('%3d' % mtrx[i], end='')
    if ((i + 1) % mtrx_sizx) == 0:
        print('')
print(f'В представленной матрице максимальным элементом среди минимальных элементов столбцов является: {max_of_min}')
