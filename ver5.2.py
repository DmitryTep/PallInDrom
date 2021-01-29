def palindrom(a = input('vvedite frazu')):
    b = a[::-1]
    c = ''
    d = ''
    for i in a:
        if i != ' ' and i != '-' and i != ',':
            c = c + i
    for j in b:
        if j != ' ' and j != '-' and j != ',':
            d = d + j
    if c == d:
        print(True)
    else:
        print(False)
palindrom()





