# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

operand_range = (2, 9)
field_range = (2, 99)
result = []
for o in range(operand_range[0], operand_range[1]+1):
    result += o, 0
    for f in range(field_range[0], field_range[1]+1):
        if f % o == 0:
            result[((o - operand_range[0]) << 1) + 1] += 1
print(f'Количество чисел В кратных числам А {operand_range} в диапазоне {field_range}. А = В:')
for i in range(operand_range[0], operand_range[1]+1):
    print(f'{result[((i - operand_range[0]) << 1)]} = {result[((i - operand_range[0]) << 1) + 1]}')
