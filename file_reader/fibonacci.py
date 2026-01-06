def fibonacci():
    arr = [0, 1]
    print(arr[0])

    for i in range(1, 10):
        c = arr[i-1] + arr[i]
        print(c)
        arr.append(c)

    # print(arr)


fibonacci()


# DSA Approach - time and space complexity


# def fibonacci(n=20):
#     arr = [0,1]

#     for i in range(2,n):
#         arr.append(arr[i-1] + arr[i-2])

#     print(arr)


# fibonacci()
