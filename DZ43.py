def y1(x):
    if x != 0:
        return  2 / x
    return 'NO'
def y2(x):
    return  (2 * x) + 3**x
x = -5
while  x >= -5 and x <= 5:
    print('*', end='\n')
    print('x = ',x)
    print('y1 = ', y1(x))
    print('y2 = ', y2(x))
    x = x + 1/2



