def count(arr):
    if arr == []:
        return 0
    else:
        return 1 + count(arr[1:])


print(count([3, 32, 33, 1, 'a', 33, '32342', ('a', 'b'), {'eewr': 'wew'}]))

