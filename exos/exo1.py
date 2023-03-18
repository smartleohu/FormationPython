import math

math.log(1)

math.log10(10)

math.exp(0)

math.cos(0)

math.cos(math.pi)

round(math.degrees(math.asin(0.5)), 2)

# 2 5 + DUP *

a, b = 2, 5

c = a + b

c_bis = c

print(c * c_bis)

# 12 0.5 SIN * 36 0.5 COS * + ABS LOG

a, b = 12, 0.5

c = math.sin(b) * a

d, e = 36, 0.5

f = math.cos(e) * d + c
print(f)

g = abs(f)
print(g)

math.log(g)
