def Binary_Search(target, data):
    start, end = 0, len(data) - 1
    data.sort()

    while start <= end:
        mid = (start + end) // 2
        if data[mid] == target: return mid
        if data[mid] < target: start = mid + 1
        else: end = mid - 1
    return -1

print(Binary_Search(10, [6, 3, 2, 10, -10])) # 예시

'''
Target: 찾을 요소, data: List
찾을 요소가 있으면 그 요소의 인덱스를(정렬된 List에서의) 없으면 -1을 반환한다.

시간 복잡도: O(log n)
'''
