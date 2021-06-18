# 3. По введенным пользователем координатам двух точек вывести уравнение прямой вида
# y = kx + b, проходящей через эти точки.

# -- SIMPLE --
x1 = float(input(f"Введите координату X точки А: ").strip())
y1 = float(input(f"Введите координату Y точки А: ").strip())
x2 = float(input(f"Введите координату X точки В: ").strip())
y2 = float(input(f"Введите координату Y точки В: ").strip())
k = (y1 - y2) / (x1 - x2)
b = y2 - k * x2
print(" y = %.2fx + %.2f" % (k, b))


# -- ADVANCED --
# def isdigit(digit):
#     try:
#         float(digit)
#         return True
#     except ValueError:
#         print(f'Ошибка! {digit} - не числовое значение.')
#         return False
#
#
# coords_len_max = 4
# coords_len = 0
# input_not_ok = 1
# can_i_div = 0
# coords = [1, 0, 0, 0]
# while input_not_ok:
#     inp = tuple(p.strip() for p in
#             input(f'Введите координаты двух точек через запятую (x1,y1,x2,y2): ').strip().split(',') if isdigit(p))
#     coords_len = len(inp)
#     if coords_len == coords_len_max:
#         for c in range(0, coords_len_max):
#             coords[c] = float(inp[c])
#         can_i_div = (coords[0] - coords[2])
#         if can_i_div != 0:
#             input_not_ok = 0
#         else:
#             print('Ошибка! Невозможно написать уравнение в заданной форме,\n'
#                   'т.к. прямая параллельна оси Y. Для данной формы х1 не может быть равен х2')
#     else:
#         print(f'Ошибка! {inp} - недостаточно координат. Ожидается {coords_len_max}')
# k = (coords[1] - coords[3]) / can_i_div
# b = coords[3] - k * coords[2]
# print(" y = %.2fx + %.2f" % (k, b))
