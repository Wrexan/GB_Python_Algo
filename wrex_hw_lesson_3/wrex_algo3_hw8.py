# 8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки
# и записывать ее в последнюю ячейку строки. В конце следует вывести полученную матрицу.


mtrx_sizx = 5
mtrx_sizy = 4
mtrx = []

for y in range(mtrx_sizy):
    mtrx_strng = [int(s) for s in input(f'Введите {y + 1}ю строку матрицы через пробел. '
                        f'Длина строки {mtrx_sizx - 1} числа: ').split()[:4]]
    mtrx_strng.append(sum(mtrx_strng))
    mtrx = [*mtrx, *mtrx_strng]

for i in range(len(mtrx)):
    print('%3d' % mtrx[i], end='')
    if ((i + 1) % mtrx_sizx) == 0:
        print('')


