class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Linked_list:

    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def print_list(self):
        temp = self.head
        while temp:
            if temp.value is not None:
                print(temp.value)
            temp = temp.next

    def pop_from_list(self):

        if self.head == None:
            return "List is empty already."

        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next

        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None

        return temp.value

    def prepend(self, value):
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def popfirst(self):
        if self.length == 0:
            print("List is empty already")
            return False
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def get(self, index):
        if index < 0 or index > self.length:
            return None

        temp = self.head

        for _ in range(index):
            temp = temp.next
        return temp

    def insert_value(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)

        new_node = Node(value)
        temp = self.get(index-1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.popfirst()
        if index == self.length-1:
            return self.pop_from_list()

        pre = self.get(index-1)
        temp = pre.next

        pre.next = temp.next
        temp.next = None
        self.length -= 1
        print(f"Removed Item {temp.value}")
        return temp


My_Linked_List = Linked_list(11)
My_Linked_List.append(3)
My_Linked_List.append(23)
My_Linked_List.append(7)
print("Current length of LL : ", My_Linked_List.length)
My_Linked_List.print_list()
print("_____####_____")
My_Linked_List.remove(2)

My_Linked_List.print_list()
print("Current length of LL : ", My_Linked_List.length)


# print(My_Linked_List.get(1))
# My_Linked_List.set_value(1, 400)

# print("Current length of LL : ",My_Linked_List.length)
# My_Linked_List.print_list()
# print("Popped item:", My_Linked_List.pop_from_list())
# print(My_Linked_List.length)
# print(My_Linked_List.pop_from_list())
# My_Linked_List.prepend("Boomi")
# print(My_Linked_List.popfirst())
# print(My_Linked_List.length)
