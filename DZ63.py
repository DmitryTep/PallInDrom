def ser():
    j = 0
    for h in b:
        return j + h

def proiz():
    i = 0
    for k in b:
        return ((i + k) / len(b))




a = [1, 2, 7, 6, 10, 3, 97, 98]
b = []
for v in a[2:8]:
    d = 2
    if v == 1:
        pass
    elif v == 2:
        b.append(v)
    elif v != d:
        while not v == d:
            d = d + 1
            if not v % d and v != d:
                break
            elif not v % d and v == d:
                b.append(v)
print(b)

c = input('введите, желаете ли продолжить?(y/n)')
if  c == 'y':
    l = input('рассчитать среднее или производную?(s/p)')
    if  l == 'p':
        print(proiz())
    else:
        print(ser())
















































