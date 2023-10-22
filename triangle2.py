import math
a = float(input("A :"))
b = float(input("B :"))
c = float(input("C (d):"))

cr = c*math.pi/180
c2 = math.sqrt(a**2 +b**2 -2*a*b*math.cos(cr))

print("c =",c2,"cm.")