def fibonacci():
    arr = [0, 1]
    print(arr[0])

    for i in range(1, 10):
        c = arr[i-1] + arr[i]
        print(c)
        arr.append(c)

    # print(arr)


fibonacci()
