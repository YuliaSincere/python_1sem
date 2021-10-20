#Вариант 3
#Сгенерируйте и выведите: Случайную строку размером 6 символов, содержащую только цифры. 
#Строка должна содержать хотя бы одну цифру 3. 

from random import choice
from string import digits

numbers = (''.join(str(choice(digits)) for i in range (6)))
while numbers.find("3") == -1:
    numbers = (''.join(str(choice(digits)) for i in range (6)))
print(numbers)



