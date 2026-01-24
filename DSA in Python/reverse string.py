# Reverse a given string using twio pointers technique


def reverse_string(string):
    str = list(string)
    L = 0
    R = len(str)-1

    while L < R:
        current = str[L]
        str[L] = str[R]
        str[R] = current
        L += 1
        R -= 1

    print(f"reversed string is {''.join(str)}")


reverse_string("Selva")
