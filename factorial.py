def squirrel(N):
    factorial = 1
    while N > 1:
        factorial *= N
        N -= 1
    factorial = str(factorial)
    emerald_nuts = factorial[0]
    return emerald_nuts
