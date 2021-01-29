def arifm(a, b, c):

    return (a + b + c)/3

uslov = input("zhelayete nachatj? (y/n)")

while uslov != 'n':
    a = int(input('vvidite pervoje chislo a'))
    b = int(input('vvedite vtoroye chislo b'))
    c = int(input('vvedite tretje chislo c'))
    print(arifm(a, b, c))
    uslov = input("prodolzhit? (y/n)")
else:
    print('spasibo za ispolzovaniye!')

