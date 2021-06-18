# 1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
# Числа и знак операции вводятся пользователем.
# После выполнения вычисления программа не должна завершаться,
# а должна запрашивать новые данные для вычислений.
# Завершение программы должно выполняться при вводе символа '0' в качестве знака операции.
# Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'),
# то программа должна сообщать ему об ошибке и снова запрашивать знак операции.
# Также сообщать пользователю о невозможности деления на ноль, если он ввел 0 в качестве делителя.

def isdigit(digit):
    try:
        if digit[:1] == '-' or digit[:1] == '+':
            float(digit[1:])
        else:
            float(digit)
        return True
    except ValueError:
        return False


def separate_2_floats(word, separator_pos):
    if isdigit(word[:separator_pos]) and isdigit(word[separator_pos + 1:]):
        return float(word[:separator_pos]), float(word[separator_pos + 1:]), 0
    else:
        print('Ошибка. Один или несколько аргументов не являются числом.')
        return 0, 1, 1


arg1 = float
arg2 = float
print('Для вычислений введите выражение. Для выхода введите 0.')
while 1:
    inp = input('>>:').replace(' ', '')
    if inp == '0':
        print('Выход...')
        break
    error = 0
    result = ''
    for i in range(0, len(inp)):
        if ((inp[i] in '+-') and i > 0) or inp[i] in '*/':
            arg1, arg2, error = separate_2_floats(inp, i)
            if error:
                result = ''
                break
            elif inp[i] == '+':
                result = int((arg1 + arg2) * 100) / 100
            elif inp[i] == '-' and i > 0:
                result = int((arg1 - arg2) * 100) / 100
            elif inp[i] == '*':
                result = int((arg1 * arg2) * 100) / 100
            elif inp[i] == '/':
                if arg2 != 0:
                    result = int((arg1 / arg2) * 100) / 100
                else:
                    print('Предотвращена попытка деления на "0"')
                    result = 'стремится к бесконечности'
    if result == '':
        print('Пожалуйста, используйте два числа и операторы "+", "-", "*", "/"')
    else:
        print(f'Результат вычислений: {inp} = {result}')
