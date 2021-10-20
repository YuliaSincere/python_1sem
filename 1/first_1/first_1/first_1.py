#a - b*c*d3+(c5-a2)/a + f3*(a-213)

res: int

print("Введите a", sep='\n')
a = int(input())
print("Введите b", sep='\n')
b = int(input())
print("Введите c", sep='\n')
c = int(input())
print("Введите d", sep='\n')
d = int(input())
print("Введите f", sep='\n')
f = int(input())

if a == 0:
    print("Деление на ноль")
else:
    res = (c**5 - a**2)/a
    result = a - b*c*(d**3) + res + (f**3)*(a-213)
    if (result < 0):
        result = 0 - result
    print("Ответ: ",result)
