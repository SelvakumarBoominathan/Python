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
        
    def append(self,value):
        new_node = Node(value)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    
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
            return "List is empty already"
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp.value
            
            
            
    def get(self, index):
        if index <0 or index >= self.length:
            print("List Index Out of Range")
            return
        temp = self.head
        
        for _ in range(index):
            temp = temp.next
            
            
        
            
        
            
              
My_Linked_List = Linked_list("Selva")
My_Linked_List.append(13)
#My_Linked_List.append(20)
My_Linked_List.print_list()
#print("Popped item:", My_Linked_List.pop_from_list())
print(My_Linked_List.length)
print(My_Linked_List.pop_from_list())
#My_Linked_List.prepend("Boomi")
print(My_Linked_List.popfirst())
print(My_Linked_List.length)


