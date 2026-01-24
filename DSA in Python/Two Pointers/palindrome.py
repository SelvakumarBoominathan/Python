def is_palindrome(string):
    # string = list(string)
    L = 0
    R = len(string)-1

    while L < R:
        if string[L] != string[R]:
            print("Given string is not a palindrome")
            break
        L += 1
        R -= 1
    else:
        # print(f'Given string "{"".join(string)}" is a palindrome.')
        print(f'Given string "{string}" is a palindrome.')


is_palindrome("madan")
