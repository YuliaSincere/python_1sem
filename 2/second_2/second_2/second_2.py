# Задан список строк, вывести все начинающиеся с r

list = ['r word word word', 'word word word',
        'r is a letter', 'russian federation']
for i in range(0, len(list)):
    list_string = list[i]
    symbol = list_string[0]
    if symbol == 'r':
        print(list_string)
