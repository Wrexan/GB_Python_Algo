# -----------------------------------------------------------------------------
#                                   Задача
# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
# (т.е. 4 отдельных числа) для каждого предприятия..
# Программа должна определить среднюю прибыль (за год для всех предприятий)
# и вывести наименования предприятий, чья прибыль выше среднего
# и отдельно вывести наименования предприятий, чья прибыль ниже среднего.
# Примечание: для решения задач попробуйте применить какую-нибудь коллекцию из модуля collections

# -----------------------------------------------------------------------------
#                                  Реализация
# import collections

year_parts = 4


def isdigit(digit):
    try:
        float(digit)
        return True
    except ValueError:
        return False


# -----------------------------------------------------------------------------
def data_input():
    companies = {}
    num_of_companies = int(input('Введите количество предприятий: '))
    for i in range(num_of_companies):
        name = input(f'Введите название предприятия №{i + 1}: ')
        companies.update({name: [float(p.strip()) for p in input
        (f'Введите прибыль "{name}" за год ({year_parts} числа через запятую): ')
                         .strip().split(',', year_parts) if isdigit(p)]})
    return num_of_companies, companies


# -----------------------------------------------------------------------------
def calc_mean(data_dict):
    _dict = data_dict.items()
    _dict_len = len(_dict)
    _aggregated = []
    _sum = 0
    for name, nums in _dict:
        _s = sum(nums)
        _aggregated.append(name)
        _aggregated.append(_s)
        _sum += _s
    mean = _sum / _dict_len
    _less_than_mean = []
    _more_than_mean = []
    for v in range(1, len(_aggregated), 2):
        if _aggregated[v] < mean:
            _less_than_mean.append(_aggregated[v - 1])
        elif _aggregated[v] > mean:
            _more_than_mean.append(_aggregated[v - 1])
    return mean, _less_than_mean, _more_than_mean


# -----------------------------------------------------------------------------
#                                      main func
def main():
    num_of_companies, companies = data_input()
    summ = calc_mean(companies)
    print('-' * 50)
    print(f'Средняя прибыль всех компаний за год: {summ[0]}\n'
          f'Компании с меньшей прибылью: {summ[1]}\n'
          f'Компании с большей прибылью: {summ[2]}')


# -----------------------------------------------------------------------------


main()
