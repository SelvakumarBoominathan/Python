mylist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]


# List Length
print(f"Length of List is : {len(mylist)}")

# list type
print(f"Type of List is : {type(mylist)}")


# list constructor
print(f"List Constructor : {list(('apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango', 'grapes'))}")

# access list items
mylist[0] = "orange"
print(f"Access List Item : {mylist[0]}")
print(f"Access List Item : {mylist[1:3]}")
print(f"Access List Item : {mylist[-1]}")   # negative indexing
print(f"Access List Item : {mylist[-3:-1]}") # negative indexing
print(f"Access List Item : {mylist[:2]}")   # slicing  - from beginning to index 3 omits last index
print(f"Access List Item : {mylist[1:]}")    # slicing