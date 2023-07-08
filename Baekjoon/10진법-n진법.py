def t2n(num, base):
    tmp = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    q, r = divmod(num, base)
    return tmp[r] if q == 0 else t2n(q, base) + tmp[r]

'''
num: 10진수 수, base: n진법
'''

print(t2n(13, 2))
