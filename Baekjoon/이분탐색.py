def Binary_Search(target, data):
    start, end = 0, len(data) - 1
    data.sort()

    while start <= end:
        mid = (start + end) // 2
        if data[mid] == target: return mid
        if data[mid] < target: start = mid + 1
        else: end = mid - 1
    return -1

print(Binary_Search(10, [6, 3, 2, 10, -10]))
