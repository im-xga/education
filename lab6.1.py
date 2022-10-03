from math import *

a=float(input("Введіть значення a: ")) 
b=float(input("Введіть значення b: ")) 
h=float(input("Введіть значення h: "))

x=a
y=0.0

for i in range( int((b - a) / h) ):
  y = ( pow(2, x) / fabs( pow(x, 2) + 1 ) ) + ( log( fabs( fabs(x) + 1 ) , 2) )
  print("%i x=%.3f y=%.3f"%(i,x,y))
  x = x + h