def GetAscii(s : str):
    re = ''
    for i in s: re += str(ord(i))
    return int(re)

def Str_Binary_Search(target, ascii, data):
    start, end = 0, len(data) - 1 

    while start <= end:
        mid = (start + end) // 2
        if data[mid] == target: return mid
        if int(GetAscii(data[mid])) < ascii: start = mid + 1
        else: end = mid - 1
    return -1


'''
아스키 코드를 이용한 문자열 버전 이분탐색
(리스트 정렬 할 때 아스키 코드를 사용한다는 것에서 착안)


- GetAscii 함수: 주어진 문자열을 아스키 코드로 나열한 숫자로 변환

매개변수 s: 아스키로 바꿀 문자열
예) '1' = 49, '11' = 4949

- Str_Str_Binary_Search 함수: 문자열 이분탐색 메인 함수

매개변수 target: 찾을 문자열, ascii: target의 아스키 코드(GetAscii를 사용해야함), data: 정렬된 문자열만 있는 리스트
찾으면 해당 인덱스를, 없으면 -1을 반환
'''


# 예제

target = '11'
Ascii = GetAscii(target) # 4949
data = sorted(['23', '11', '32', '0', '10', '5']) # ['0', '10', '11', '23', '32', '5']

print(Str_Binary_Search(target, Ascii, data))
