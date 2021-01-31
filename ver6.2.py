n = int(input('vvedite chislo shodinok'))
h = []
for b in range(0, n + 1):
    for a in range(0, n + 1):
        if (2 * b) + a == n:
            h.append(a)
            h.append(b)
print(h)







































