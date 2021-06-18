# 4. Написать программу, которая генерирует в указанных пользователем границах:
# случайное целое число;
# случайное вещественное число;
# случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона.
# Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
# Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.

point_1 = float(input("Введите первый предел: "))
point_2 = float(input("Введите второй предел: "))
if point_2 < point_1:
    point_1, point_2 = point_2, point_1
diff = point_2 - point_1

if diff != 0:
    result = point_1 + abs(point_1 * 2 - point_2 ** 1.2) % diff
else:
    result = point_1
print(result)
print(f"Случайное целое число в заданных пределах: {int(result)}")
print(f"Случайное вещественное число в заданных пределах: {result}")
print(f"Случайный символ число в заданных пределах: {chr(int(result + 96))}")


# import random
#
# point_1 = float(input("Введите первый предел: "))
# point_2 = float(input("Введите второй предел: "))
# if point_2 < point_1: point_1, point_2 = point_2, point_1
# diff = point_2 - point_1
#
# print(f"Случайное целое число в заданных пределах: {random.randint(int(point_1), int(point_2))}")
# print(f"Случайное вещественное число в заданных пределах: {random.uniform(point_1, point_2)}")
# print(f"Случайный символ в заданных пределах: {chr(int(random.random() * diff + 96 + point_1))}")
