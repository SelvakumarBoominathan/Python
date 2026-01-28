

def addtion_of_list(list):
    if len(list) == 0:
        return 0
    else:
        return list[0] + addtion_of_list(list[1:])


print(addtion_of_list([1, 2, 3, 4, 5]))
