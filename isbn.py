import math
number = input("ISBN: ")
filled = number.zfill(9)
# number2 = int(filled)
x = [int(p) for p in filled]

a,b,c,d,e,f,g,h,i = x

isbn = 10*a + 9*b +8*c + 7*d + 6*e + \
        5*f + 4*g + 3*h + 2*i

total1 = isbn%11
n = 11-total1
if n == 10:
    n = 0
n10 = str(n)
z = a,b,c,d,e,f,g,h,i
convert = ''.join(map(str,z))

print(convert+n10)