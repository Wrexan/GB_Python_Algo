# 3. По введенным пользователем координатам двух точек вывести уравнение прямой вида
# y = kx + b, проходящей через эти точки.

def isdigit(digit):
    try:
        float(digit)
        return True
    except ValueError:
        return False


coords_len_max = 4
coords_len = 0
input_not_ok = 1
can_i_div = 0
coords = [1, 0, 0, 0]
while input_not_ok:
    inp = tuple(p.strip() for p in
                input(f'Введите координаты двух точек через запятую (x1,y1,x2,y2): ').strip().split(',') if isdigit(p))
    coords_len = len(inp)
    print(inp)
    if coords_len == coords_len_max:
        for c in range(0, coords_len_max):
                coords[c] = float(inp[c])
        can_i_div = (coords[0] - coords[2])
        if can_i_div != 0:
            input_not_ok = 0
k = (coords[1] - coords[3]) / can_i_div
b = coords[3] - k * coords[2]
print(" y = %.2fx + %.2f" % (k, b))
