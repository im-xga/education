from math import *

x=float(input("Задайте x: "))
y=0.0
if x>=5.1:
  y=log(3*x, 2) - 7*sqrt(x)
elif x>-0.7 and x<5.1:
  y=pow(e, x) + 2*pow(x, 3)
elif x<=-0.7:
  y=pow(e, x) + sin(x+pi/4)

print("y =", y)