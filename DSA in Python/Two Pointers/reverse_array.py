def reverse_array(arr):
    L = 0
    R = len(arr)-1

    while R > L:
        arr[L], arr[R] = arr[R], arr[L]
        L += 1
        R -= 1
    return arr


print(reverse_array(["a", "e", "i", "o", "u"]))
