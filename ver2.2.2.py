x = int(input("vvedite x:"))
y = int(input("vvedite y:"))
d = input("deistvire:")

if  d == "/" and y == 0:
    print("Ошибка")
elif d == "/":
    r1 = x / y
    print(r1)
elif d == "-":
    r1 = x - y
    print(r1)
elif d == "+":
    r1 = x + y
    print(r1)
elif d == "*":
    r1 = x * y
    print(r1)





