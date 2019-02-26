def sum(arr):
    if arr == []:
        return 0
    else:
        return arr[0] + sum(arr[1:])


print(sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

