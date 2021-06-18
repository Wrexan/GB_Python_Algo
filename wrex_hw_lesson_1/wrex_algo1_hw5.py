# 5. Пользователь вводит две буквы.
# Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.

letter_template = 'abcdefghijklmnopqrstuvwxyz'
letter_1 = input('Введите лубую букву латинского алфвита: ').lower()
idx1 = letter_template.find(letter_1)
letter_2 = input('Введите еще одну букву латинского алфвита: ').lower()
idx2 = letter_template.find(letter_2)
print(f'Позиция буквы {letter_1} = {idx1 + 1}\n'
      f'Позиция буквы {letter_2} = {idx2 + 1}\n'
      f'Букв между ними = {abs(idx2 - idx1) - 1}')

