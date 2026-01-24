#Fine a pair in a sorted array such that their sum is equal to a given number
#using Two Pointers Technique


arr = [2,3,5,7,9,11,12,13]

target = 10
pointers = []
L = 0
R = len(arr)-1

while L < R:
    current_sum = arr[L] + arr[R]
    
    if current_sum == target:
        pointers.append(L)
        pointers.append(R)
        print(f"Sum is : {current_sum}, pointers are {pointers}")
        break
    elif current_sum > target:
        R -=1
    else:
        L+=1
else:
    print("No value found")





