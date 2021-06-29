# -----------------------------------------------------------------------------
#                                   Задача
# 4.2 Написать два алгоритма нахождения i-го по счёту простого числа.
# Без использования Решета Эратосфена;
# Использовать алгоритм решето Эратосфена
#
# Проанализировать скорость и сложность алгоритмов.
# Результаты анализа сохранить в виде комментариев в файле с кодом.

# -----------------------------------------------------------------------------
#                                  Примечание
# Тест с использованием решета эратосфена и брут форса. Выборка чисел до 100_000.
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.001    0.001   77.248   77.248 <string>:1(<module>)
#         1    0.038    0.038    0.039    0.039 wrex_algo4_hw2.py:106(simples_ert)
#         1   77.143   77.143   77.147   77.147 wrex_algo4_hw2.py:123(simples_bf)
#         1    0.001    0.001   77.247   77.247 wrex_algo4_hw2.py:144(main)
#         2    0.039    0.019    0.061    0.030 wrex_algo4_hw2.py:96(zeroton_get)
#         1    0.000    0.000   77.248   77.248 {built-in method builtins.exec}
#         2    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         2    0.000    0.000    0.000    0.000 {built-in method builtins.print}
#    219186    0.026    0.000    0.026    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# Решето Эратосфена позволяет предсказывать заведомо непростые числаи исключить их из дальнейших рассчетов,
# чем сокращает количество операций проверки и избаляет от деления.
# В случае с перебором каждое число списка требует n-3 делений, что очень растратно.

# -----------------------------------------------------------------------------
#                                  Реализация

import cProfile

simples_limit = 10_000


def zeroton_get(n):
    ztn = []
    for i in range(n + 1):
        ztn.append(i)
    ztn[1] = 0
    return ztn


# -----------------------------------------------------------------------------
#                                    Вариант 1
def simples_ert(ztn):
    m = 2
    n = len(ztn)
    sl = []
    while m < n:
        if ztn[m] != 0:
            j = m * 2
            while j < n:
                ztn[j] = 0
                j += m
            sl.append(m)
        m += 1
    return sl


# -----------------------------------------------------------------------------
#                                     Вариант 2
def simples_bf(ztn):
    m = 2
    n = len(ztn)
    sl = []
    while m < n:
        j = 2
        is_simple = 1
        while j < m:
            if ztn[m] % ztn[j] == 0:
                is_simple = 0
                break
            j += 1
        if is_simple == 1:
            sl.append(m)
        m += 1
    return sl


# -----------------------------------------------------------------------------
#                                      main func

def main():
    zeroton_seq = zeroton_get(simples_limit)
    print(simples_ert(zeroton_seq)[0])
    zeroton_seq = zeroton_get(simples_limit)
    print(simples_bf(zeroton_seq)[0])


# -----------------------------------------------------------------------------
#                                   Вывод результата

cProfile.run('main()')
