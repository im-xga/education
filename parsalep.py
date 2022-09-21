import sys
a = float(sys.argv[1]) 
b = float(sys.argv[2]) 
h = float(sys.argv[3]) 
S=2*(a*b+a*h+b*h)
V=a*b*h
print("Площа= ",S)
print("Об'єм= ",V)
