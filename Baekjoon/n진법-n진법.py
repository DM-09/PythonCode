def n2n(num, base, base2, b=False):
    tmp = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    num2 = num if b else int(num, base)
    q, r = divmod(num2, base2)
    return tmp[r] if q == 0 else n2n(q, 0, base2, True) + tmp[r]

'''
num: n진수(str), base: num의 진법, base2: 내가 바꾸고 싶은 n진법
'''

print(n2n('a', 16, 2))
