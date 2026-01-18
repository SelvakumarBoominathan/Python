mylist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]


# List Length
print(f"Length of List is : {len(mylist)}")

# list type
print(f"Type of List is : {type(mylist)}")


# list constructor
print(
    f"List Constructor : {list(('apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango', 'grapes'))}")

# access list items
mylist[0] = "orange"
print(f"Access List Item : {mylist[0]}")
print(f"Access List Item : {mylist[1:3]}")
print(f"Access List Item : {mylist[-1]}")   # negative indexing
print(f"Access List Item : {mylist[-3:-1]}")  # negative indexing
# slicing  - from beginning to index 3 omits last index
print(f"Access List Item : {mylist[:2]}")
print(f"Access List Item : {mylist[1:]}")    # slicing

# check if item exists  (in & not in)
if "banana" not in mylist:
    print("No, 'banana' is not in the fruits list")

if "banana" in mylist:
    print("Yes, 'banana' is in the fruits list")


# Change range of List Items
mylist[1:3] = ["blackcurrant", "watermelon"]
print(f"Change range of List Items : {mylist}")

# Note: The number of items you insert does not need to match the number of items you replace.
# Example: if you insert 2 items, but remove 3 items, the new list will have one item less.
mylist[1:4] = ["grapes"]
print(f"Change range of List Items : {mylist}")


# Insert Items
mylist.insert(2, "guvava")  # insert will add item at the specified index
print(f"Insert Items : {mylist}")


# Append Items
mylist.append("pineapple")  # append will add item at the end of the list
print(f"Append Items : {mylist}")

# Extend List
# add any iterable object to list using extend()
tropical = ["mango", "papaya", "mango", "pataya"]
mylist.extend(tropical)
print(f"Extend List : {mylist}")


# Remove List Items
# removes specified item. if the item is not found, it will raise a ValueError
mylist.remove("mango")
# mylist.remove(1)
print(f"Remove List Items : {mylist}")
# removes item at specified index (or first item appearance if index not specified)


# removes the last item by default else removes item at specified index
mylist.pop()
mylist.pop(1)  # removes item at index 1
print(f"Pop List Items : {mylist}")


# clear the list
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(f"Clear List : {thislist}")


# delete list items using del keyword
mylist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
del mylist[0]
print(f"Delete List Items using del : {mylist}")

# delete entire list
del mylist
# print(f"Delete entire List using del : {mylist}")  # this will raise an error as the list is deleted


# Loop through a list
mylist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
for x in mylist:
    print(f"Loop through List : {x}")

# Loop through list using index
for i in range(len(mylist)):
    print(f"Loop through List using index : {mylist[i]}")


# Loop through list using while
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1


# List Comprehension
# newlist will contain all items from mylist that have the letter "a" in them
newlist = [x for x in mylist if "a" in x]
print(f"List Comprehension : {newlist}")

# Sort List
# sort() method sorts the list ascending by default. It changes the original array and returns nothing
mylist.sort()   # sort list in ascending order
print(f"Sort List : {mylist}")
mylist.sort(reverse=True)  # sort list in descending order
print(f"Sort List in Descending order : {mylist}")
