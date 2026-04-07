#задача 1
'''
a = int(input("Введите число: "))
b = float(input("Введите число: "))

print("a   ", a, b)

c = a
a = b
b = c
print("b   ",a,b)

print("c   ", a+b ,a-b ,a*b)
'''
#задача 2
'''
c = input("Введите строку: ")
b = input("Введите строку: ")
a = input("Введите число: ")

print("a   ", a+b, a+c, b+c)

print("b   ", type(int(a)), int(a))

e = input("Введите симвл: ")
print("c   ", e in b)

print(c.upper(), c.lower())
'''
#задача 3
'''
import random

a = random.randint(-100, 100)
b = random.randint(-100, 100)

c = int(input("Введите число: "))

if a<b and c<=b and c>=a:
    print(f"Вы попали в диаппазон {a}:{b}")
elif b<a and c<=a and c>=b:
    print(f"Вы попали в диаппазон {b}:{a}")
else:
    print(f"Вы НЕ попали в диаппазон {min(a,b)}:{max(a,b)}")
'''
#задача 4
'''
a = int(input("Введите число: "))

if a==0: print("число равно нулю")
elif a>0:
    print(a+100)
    if a%2 == 0:
        print(a*2)
else:
     print(a-100)
     if a%2==1:  print(a**2)
'''
#задача 5
'''
a = input("Введите свою фамилию: ")
b = input("Введите своё имя: ")

print(f"Привет, {b} {a}!")
print(len(a), len(b))
'''
#задача 6
'''
a = [" (o o) ", "  /V\  ", " /(_)\ ", " ^^ ^^ "]

c = int(input("Введите число: "))

for i in range(4):
    print(a[i]*c)
'''
#задача 7
def animal(year):
    animals = ["Крысы", "Быка", "Тигра", "Кролика", "Дракона", "Змеи","Лошади", "Козы", "Обезьяны", "Петуха", "Собаки", "Свиньи"]
    return animals[(year - 4) % 12]

year = int(input("Введите год: "))
print(f"{year} — год: {animal(year)}")

