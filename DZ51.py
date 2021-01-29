def rec(n,c):
    if n == c:
        return n
    else:
        return c + rec(n,c - 1)


print(rec(6,9))
