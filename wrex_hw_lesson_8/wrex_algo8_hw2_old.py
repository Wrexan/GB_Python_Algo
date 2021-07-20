# -----------------------------------------------------------------------------
#                                   Задача
# 8.2 Закодируйте любую строку из трех слов по алгоритму Хаффмана.
# -----------------------------------------------------------------------------
# Для полноценной проверки нужны повторяющиеся символы.
# Для большей наглядности и сокращения объема данных исходный букварь ограничен символами ABCDEFGH
#
# -----------------------------------------------------------------------------
#                                     Данные
import random

string = 'mama myla ramu'
word_1 = ['Аист', 'Берёза', 'Вася', 'Годзилла', 'Дочка',
          'Ёжик', 'Жена', 'Зёбра', 'Игнат', 'Кеша',
          'Ласка', 'Мама', 'Носорог', 'Петя', 'Тётя']
word_2 = ['Аист', 'Берёза', 'Вася', 'Годзилла', 'Дочка',
          'Ёжик', 'Жена', 'Зёбра', 'Игнат', 'Кеша',
          'Ласка', 'Мама', 'Носорог', 'Петя', 'Тётя']
word_3 = ['Аист', 'Берёза', 'Вася', 'Годзилла', 'Дочка',
          'Ёжик', 'Жена', 'Зёбра', 'Игнат', 'Кеша',
          'Ласка', 'Мама', 'Носорог', 'Петя', 'Тётя']


def rnd(a: str, b: str, c: str):
    return[a[random.randint(0, len(a))], ' ', b[random.randint(0, len(b))], ' ', c[random.randint(0, len(c))]]


# -----------------------------------------------------------------------------
#                                    Генератор весов
def get_weights(st: string):
    symbols, weights, add = [], [], False
    str_l = len(st)
    for str_n in range(str_l):
        for sn in range(len(symbols)):
            if st[str_n] == symbols[sn]:
                weights[sn] += 1
                add = True
                break
        if not add:
            symbols.append(st[str_n])
            weights.append(1)
            # print(f'{symbols=} {weights=}')
        else:
            add = False
    return symbols, weights


# -----------------------------------------------------------------------------
#                                    Упорядочивание
def merge_sort(st: list, wt: list):
    if len(wt) <= 1 or len(wt) != len(st):
        return
    left_w, right_w = wt[:len(wt) // 2], wt[len(wt) // 2:]
    left_s, right_s = st[:len(st) // 2], st[len(st) // 2:]
    # print(f'{left_s=} {left_w=} {right_s=} {right_w=}')
    merge_sort(left_s, left_w)
    merge_sort(right_s, right_w)
    n = m = k = 0
    center_w = [0] * (len(left_w) + len(right_w))
    center_s = center_w.copy()
    while n < len(left_w) and m < len(right_w):
        if left_w[n] <= right_w[m]:
            center_w[k] = left_w[n]
            center_s[k] = left_s[n]
            n += 1
        else:
            center_w[k] = right_w[m]
            center_s[k] = right_s[m]
            m += 1
        k += 1
    while n < len(left_w):
        center_w[k] = left_w[n]
        center_s[k] = left_s[n]
        n += 1
        k += 1
    while m < len(right_w):
        center_w[k] = right_w[m]
        center_s[k] = right_s[m]
        m += 1
        k += 1
    for i in range(len(wt)):
        wt[i] = center_w[i]
        st[i] = center_s[i]
    return st, wt


# -----------------------------------------------------------------------------
#  Распускаем стринг на подстринги, проверяем часть в общем через хеш, исключаем повтор
# def


# -----------------------------------------------------------------------------
#                                      main func
def main(st: string):
    s_list, w_list = get_weights(st)
    print(f'{s_list=} {w_list=}')
    s_list, w_list = merge_sort(s_list, w_list)
    print(f'{s_list=} {w_list=}')


# -----------------------------------------------------------------------------
#
main(string)
