def SOE(MAX, MIN=1):
    box, l = [], [i + 1 for i in range(MAX)]

    for i in range(MAX):
        c = l[i]
        if c != 1 and c != 0:
            for j in range(2, MAX // c + 1):
                l[c * j - 1] = 0
            if c >= MIN: box.append(c)
    return box

'''
[설명]
에라토스테네스의 체, 특정 범위의 소수들을 모두 구하여 리스트로 반환함

[매개변수]
MAX: 정수, 최댓값(이 수 까지의 소수를 찾음), 필수
MIN: 정수, 최솟값(이거 보다 크거나 같은 소수만 걸러짐), 기본값 1

[시간복잡도] O(n)
'''

# 예제
print(SOE(10)) # [2, 3, 5, 7]
