# 8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.
source = ''
source_length = int(input('Сколько чисел для поиска хотите ввести?: ').replace(' ', ''))
if source_length > 10:
    source_length = 10
    print('Слишком много чисел, установлено 10')
for i in range(source_length):
    source += input('Введите число: ').replace(' ', '')
    if (i + 1) < source_length:
        source += ', '
operand = input(f'Введите цифру для поиска в {source}: ').replace(' ', '')

print(f'В числах\n{source}\nцифра {operand} встречается {source.count(operand)} раз')
