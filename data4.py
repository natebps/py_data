v1,v2,v3 = [float(e) \
            for e in input("a:").split()]
u1,u2,u3 = [float(e) \
            for e in input("b:").split()]
dotp = v1*u1 + v2*u2 + v3*u3
print(dotp)

