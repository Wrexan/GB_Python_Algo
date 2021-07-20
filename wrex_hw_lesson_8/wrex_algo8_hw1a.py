# -----------------------------------------------------------------------------
#                                   Задача
# 8.1 Определить количество различных подстрок с использованием хеш-функции.
# Задача: на вход функции дана строка, требуется вернуть количество различных подстрок в этой строке.
# Примечание: в сумму не включаем пустую строку и строку целиком.
# -----------------------------------------------------------------------------
# Для полноценной проверки нужны повторяющиеся символы.
# Для большей наглядности и сокращения объема данных исходный букварь ограничен символами ABCDEFGH
#
# -----------------------------------------------------------------------------
#                                     Данные
import random
import hashlib

ra_limin = 65  # A
ra_limax = 72  # H
ra_size = 10


# -----------------------------------------------------------------------------
#                                    Генератор строки
def rnd(size, limit_1, limit_2):
    ra = []
    rs = ''
    for i in range(size):
        ra.append(chr(random.randint(limit_1, limit_2)))
    return rs.join(ra)


# -----------------------------------------------------------------------------
#                                    Поиск подстринга в стринге
def rabin_karp(s, t):
    len_sub = len(t)
    h_subs = hashlib.sha1(t.encode('utf-8')).hexdigest()
    for i in range(len(s) - len_sub + 1):
        if h_subs == hashlib.sha1(s[i:i + len_sub].encode('utf-8')).hexdigest():
            return i
    return -1


# -----------------------------------------------------------------------------
#  Распускаем стринг на подстринги, проверяем часть в общем через хеш, исключаем повтор
def string_of_strings(s):
    s_len = len(s)
    result = []
    for ss_len in range(1, s_len):
        for ss_pos in range(0, s_len):
            if ss_pos <= s_len - ss_len:
                ss = s[ss_pos:ss_pos + ss_len]
                if hashlib.sha1(ss.encode('utf-8')).hexdigest() not in result:
                    rk = rabin_karp(s, ss)
                    # print(f'{ss_pos=} {ss_len=} {ss=} {rk=}')
                    if rk >= 0:
                        result.append(hashlib.sha1(ss.encode('utf-8')).hexdigest())
    return result


# -----------------------------------------------------------------------------
#                                      main func
def main():
    string = rnd(ra_size, ra_limin, ra_limax)  # создаем стринг
    print(f'string: {string}')  # выводим стринг

    res = string_of_strings(string)  # создаем список подстрингов по условию задачи

    for i in range(len(res)):  # выводим подстринги в удобном виде
        print('%10s' % res[i], end='|')
        if ((i + 1) % 5) == 0:
            print('')
    print(f'\nКоличество уникальных строк: {len(res)}')  # выводим стринг


# -----------------------------------------------------------------------------
#
main()
