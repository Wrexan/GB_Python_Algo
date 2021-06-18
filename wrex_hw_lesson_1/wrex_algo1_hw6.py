# 6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

letter_template = 'abcdefghijklmnopqrstuvwxyz'
idx = int(input('Введите номер буквы латинского алфвита: '))
letter = letter_template[idx-1]

print(f'Вы выбрали букву: {letter}')

