class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self.size +=1
    def to_list(self):
        current = self.head
        result = []
        while current is not None:
            result.append(current.data)
            current = current.next 
        return result
        
    def __len__(self):
        return self.size
    
            
            
ll = LinkedList()
ll.append(5)
print(ll.head is ll.tail)   # True
ll.append(7)
print(ll.head is ll.tail)   # False
print("Length:", ll.__len__())
for value in ll.tolist():
    print(value)