import math

x = float(input("Numbers: "))
y = 2 - x + (3/7)*x**2 - (5/11)*x**3 + \
    math.log10(x)

print("total : ",y)