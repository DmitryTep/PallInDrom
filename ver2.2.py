import math
x = input('введіть х')
y = input('введіть у')
x = int(x)
y = int(y)
print('x=',x,'y=',y)
if x >= -math.pi and x <= math.pi:
    y = math.cos(3*x)
    print('y = ',y)
elif x < -math.pi or x > math.pi:
    y = x
    print('y =',y)



