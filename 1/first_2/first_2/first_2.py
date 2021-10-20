# Выведите все нечетные элементы в одной строке.
list = [1,"кот",3,4,5,"рыбка",7,8,"кролик",10] 
list_result = []
for i in range (0,len(list)):
    if list.index(list[i])%2 == 0:
        list_result.append(list[i])
        # print(list[i])
print(list_result)





