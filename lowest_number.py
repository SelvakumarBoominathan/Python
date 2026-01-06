arr = [4, 3, 5, 6, 33, 7, 22, 90]


def lowest_num(arr):
    lowest = arr[0]
    for i in range(len(arr)):
        if arr[i] < lowest:
            lowest = arr[i]
    return lowest


print(lowest_num(arr))
