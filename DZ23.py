import math
print('ax**2 + bx+ c = 0')
a = int(input('VVedite a'))
b = int(input('Vvedite b'))
c = int(input('Vvedite c'))
discr = pow(b,2) - (4*a*c)
print(discr)
if discr < 0:
    print('Коренів немає')
elif not discr:
    x = -b / (2*a)
    print('Єдиний х = ',x)
else:
    x1 = (-b + pow(discr,1/2))/(2*a)
    x2 = (-b - pow(discr,1/2))/(2*a)
    print(pow(discr,1/2))
    print("Рівняння має два корені:"
          "x1 = ",x1, "x2 = ",x2)









