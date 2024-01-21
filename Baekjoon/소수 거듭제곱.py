def dpow(d:str, b:int):
    a = int(d.replace('.', ''))

    tail = len(d[d.index('.')+1:])
    mul = str(a ** b)
    n = len(mul) - tail * b

    l = mul[:n]
    r = mul[n:]

    if d[0] == '0':
        l = '0'; r = mul
        r = '0' * (tail * b - len(r)) + r
    return l + '.' + r
