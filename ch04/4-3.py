def max_num(arr):
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    sub_max = max_num(arr[1:])
    return arr[0] if arr[0] > sub_max else sub_max


print(max_num([13, 354, 122, 12, 556, 21, 323]))

