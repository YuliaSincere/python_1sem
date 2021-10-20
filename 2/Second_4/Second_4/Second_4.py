#Пусть дана строка:На основе данной строки сформируйте новую, содержащую только буквы Л. Выведите новую строку.
print("Введите строку")
userString = input()
result = []
for i in userString:
    if i == "л":
        result.append(i)
print("".join(result))

