from math import *
def func1(x, y, z):
  R= 12 * (pow(x, 2) + sin(y)) + ( sqrt( pow(z, 2) + 1 ) / log(fabs(fabs(z) + 0.07), 3) )
  return(R)
x=float(input("Введіть x: "))
y=float(input("Введіть y: "))
z=float(input("Введіть z: "))
result=func1(x, y, z)
print(result)