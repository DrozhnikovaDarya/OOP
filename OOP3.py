#Задача 1
"""
def summ(A):
    #S = sum(A)
    S = 0
    for i in A:
        S += i
    print(f'Сумма: {S}')
    return: S

def kv(A):
    B = A.copy()
    for i in range(len(A)):
        if A[i] < 0 and A[i] % 2 == 0:
            B[i] = A[i]**2
    print(B)

def raz(A):
    n = 100
    m = -100
    for i in A:
        if i > m: m = i
        if i < n: n = i
    print(f"Максимальное число: {m}, минимальное число: {n}. Их разность: {m-n}")

a = input("Введите число: ")
A = []

while a!="end":
    A.append(int(a))
    a = input("Введите число: ")
    
print(f"Изначальный массив: {A}")    
summ(A)
kv(A)
raz(A)
"""

#Задача 2
"""
def T(n,m,x,y):
    if x>n and y<m:
        print(f"Диапаон {x}:{y} лежит в {n}:{m}")
        
n, m = input("Введите границы диапазона: ").split(" ")
x, y = input("Введите границы диапазона: ").split(" ")

T(n,m,x,y)
"""

#Задача 3
"""
def T(n):
    for i in range(1,11):
        print(f"{n} * {i} = {n*i}")
        
n = int(input("Введите число: "))
T(n)
"""

#Задача 4
"""
def T(a,b,c):
    a1 = [a[0],b[0],c[0]]
    b1 = [a[1],b[1],c[1]]
    c1 = [a[2],b[2],c[2]]
    print(a1)
    print(b1)
    print(c1)
    
a = [1,2,3]
b = [4,5,6]
c = [7,8,9]
T(a,b,c)
"""

#Задача 5
"""
def tr(a,b):
    for i in range(1,a//2+2):
        print(b*i," ")
    for i in range(a//2,0,-1):
        print(b*i," ")
    

a = int(input("Введите основание треугольника: "))
b = input("Введите симбол: ")
b += "  "

tr(a,b)
"""

#Задача 6
"""
def T(a):
    zif = []
    buk = []
    for i in a:
        if i in ['0','1','2','3','4','5','6','7','8','9']:
            zif.append(int(i))
        else:
            buk.append(i)
    print(zif)
    print(buk)
    
a = input("Введите список через пробел: ").split(" ")

T(a)
"""

#Задача 7
"""
def summ(a,b):
    c = a.copy()
    for i in range(2):
        for t in range(2):
            c[i][t] = a[i][t] + b[i][t]
   
    print(c)
    
a = [[1,2,3], [4,5,6], [7,8,9]]
b = [[11,12,13], [14,15,16], [17,18,19]]


summ(a,b)
"""

#Задача 8
"""
def update(objects_list, attr_name, new_age):
    for i in objects_list:
        setattr(i, attr_name, new_age)
            
class CAT:
    #атрибуты
    def __init__ (self, name, long, age, mustache, colors):
        self.name = name
        self.long = long
        self.age = age
        self.mustache = mustache
        self.colors = colors
    
    def voice(self):
        print(f"{self.name} говорит мяяяу!")
    def bark(self):
        print(f"{self.name} быстро убегает от разбитого горшка!")
    def jump(self):
        print(f"{self.name} прыгает на шкаф и на всех осуждающе смотрит")
    def hunger(self):
        print(f"{self.name} громко мяукает и требует еды")
    def fight(self,target):
        print(f"{self.name} трескает {target.name}, за что получает тапком по ушам")
    def sleep(self):
        print( f"{self.name} сладко спит пять часов подряд и жалкие люди завидуют ему/ей")
        
cat1 = CAT("Муся", 0.5, 17, "длинные и мягкие", "серенькая с белыми носочками")
cat2 = CAT("Рыжый", 0.6, 8, "длинные и упругие", "рыжик")

print(cat1.__dict__)
print(cat2.__dict__)

cat1.sleep()
cat2.fight(cat1)

update([cat1], "age", 19)
print(cat1.__dict__)
"""
