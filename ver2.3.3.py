import math
x = 2
print(math.pi)
if x >= -math.pi and x <= math.pi:
   y = math.cos(3*x)
   print(y)
elif x < -math.pi or x > math.pi:
    y = x
    print(y)