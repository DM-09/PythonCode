def fpow(a, b):
    r = 1
    while b:
        if b % 2: r *= a
        a *= a
        b //= 2
    return r

# 예제
print(fpow(2, 3) # 8

'''
[분할정복을 이용한 빠른 거듭제곱]
시간 복잡도: O(log n)

매개변수: a, b 모두 숫자여야함, 각각 밑, 지수를 의미함
'''
