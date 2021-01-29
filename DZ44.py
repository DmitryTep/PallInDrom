def mnozh(a,b):
    return a * b
def delen(a,b):
    if b:
        return a / b
    else:
        return "Nelza delitj na nolj"
def plus(a,b):
    return a + b
def minus(a,b):
    return a - b
uslov = input('nachnem?(y/n)')
while uslov != 'n':
    a = int(input('vvedite a'))
    b = int(input('vvedite b'))
    c = input('vvedite deistvie')
    if c =='+':
        print(plus(a,b))
    elif c =='/':
        print(minus(a,b))
    elif c =='*':
        print(mnozh(a,b))
    elif c == '-':
        print(minus(a,b))
    elif c == 'quit':
        print("spasibo!")
        break
