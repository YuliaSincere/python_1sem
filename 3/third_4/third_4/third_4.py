#Вариант 3
#Пусть дана строка произвольной длины. Выведите информацию о том, сколько в ней символов и сколько слов.

#Запрашиваем строку
print("Введите строку")
user_string = input()

#Считаем символы
user_string_len = len(user_string)
#Считаем слова с помощью возвращения количества вхождений подстроки в строку
# +1 из-за того, что первое слово не начинается с пробела
if user_string.startswith(" "):
    user_string_word = user_string.count(" ")
else:
    user_string_word = user_string.count(" ") + 1

print("Количество символов: " + str(user_string_len))
print("Количество слов: " + str(user_string_word))

