def decimal_format(n, d):
    return float(f"{{:.{d}f}}".format(n))

'''
[소수점 자리수 제한 함수]
n : 해당 숫자(int, float)
d : 제한할 범위(int) ex. 3이면 소수점 세 자리까지
'''

print(decimal_format(3.21356, 2)) # 예제
# 3.21
