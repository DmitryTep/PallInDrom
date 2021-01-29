def palindrom(a):
    if len(a) < 1:
        return True
    else:
        if a[0] == a[-1]:
            return palindrom(a[1:-1])

t = str(input('vvedite stroku: '))
if palindrom(t) == True:
    print('Паліндром!')
else:
    print('Не паліндром!!!!')





































