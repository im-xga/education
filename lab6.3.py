from math import *

a=float(input("Введіть значення a: ")) 
b=float(input("Введіть значення b: ")) 
h=float(input("Введіть значення h: "))

x=a
y=0.0

spisok=[]
while x<b:
  y = ( pow(2, x) / fabs( pow(x, 2) + 1 ) ) + ( log( fabs( fabs(x) + 1 ) , 2) )
  spisok.append(y)
  x = x + h

print()
print("Список:")
for i in range(0, len(spisok)):
  print(spisok[i])

print()
print("Найменше значення функції на заданому проміжку: ", spisok[0])
print("Найбільше значення функції на заданому проміжку: ", spisok[len(spisok)-1])