def permute(arr):
    if len(arr) in [0, 1]:
        return [arr]

    res = []

    for i in range(len(arr)):
        rest_arr = arr[:i] + arr[i + 1:]
        for other in permute(rest_arr):
            res.append([arr[i]] + other)

    return res
