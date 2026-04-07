#Задача 1
"""
import random

a = int(input("Введите длину списка: "))
B = []


for i in range(a):
  B.append(random.randint(-100,100))

print('Изначальный список: ',B)
print('a   ',[i**2 for i in B])
print('b   ',[i for i in B if i>0 and i%2==0], len([i for i in B if i>0 and i%2==0]))
print('c   ',[i for i in B if i<0 and i%2==1], len([i for i in B if i<0 and i%2==1]))
"""
#Задача 2
"""
a = input('Введите число: ')
S = 0

while a!='end':
    S+=int(a)
    print('Сумма: ', S)
    a = input('Введите число: ')
"""
#Задача 3
"""
a = int(input('Введите длину списка: '))
B = []
  
for i in range(a):
  B.append( int(input('Введите элемент: ')))
  
print(B)
print('a   ', sorted(B))
print('b   ', sorted(B)[::-1])
print('c   ', min(B))
print('d   ', max(B))
"""

#Задача 4
"""

import random

def W(a):
  A = []
  for i in range(a):
    A.append(random.randint(-100,100))
  return set(A)


A = W(int(input("Ведите длину списка: ")))
B = W(int(input("Ведите длину списка: ")))
C = W(int(input("Ведите длину списка: ")))

D = A|B|C
print(A, B, C)
print(D)
print(sorted(D))
print(sorted(D)[::-1])
"""

#Задача 5
"""
a = sorted(list(input('Введите слово: ')))
b = sorted(list(input('Введите слово: ')))

print("Слова являются аннограммой" if a==b else "Слова НЕ являются аннограммой")
"""

#Задача 6
"""
a = input('Введите слово: ').split(" ")
b = input('Введите слово: ').split(" ")


print([i for i in a if i in b] )
"""

#Задача 7
"""
import random

a = int(input("Введите число: "))
b = random.randint(-100, 100)


while a != b:
        if a>b: print("Загаданное число меньше вашего")
        else: print("Загаданное число больше вашего")
        a = int(input("Введите число: "))
        
print("Вы угадали число!!!")
"""

#Задача 8
"""
a = input('Введите интересы первого человека: ').split(", ")
b = input('Введите интересы второрго человека: ').split(", ")


C = [i for i in a if i in b] 

print(len(C)/(len(a)+len(b))*100, "%")
"""

#Задача 9
a = input("Введите ключи через пробел: ").split(" ")
b = input("Введите значения массива через пробел: ").split(" ")
print(dict(zip(a, b)))