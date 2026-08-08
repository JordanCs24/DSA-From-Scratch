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
    def prepend(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size +=1
    def search(self,data):
        
        current = self.head
        index = 0
        
        while current is not None:
            if current.data == data:
                return index 
            current = current.next 
            index += 1
        return -1
        
    def __len__(self):
        return self.size
    
            
            
ll = LinkedList()
ll.append(5)
print(ll.head is ll.tail)   # True
ll.append(7)
print(ll.head is ll.tail)   # False
print("Length:", ll.__len__())
ll.prepend(10)
ll.append(15)
ll.append(13)
ll.prepend(1)
for value in ll.to_list():
    print(value)

print("Search for 1: ", ll.search(1))
print("Search for 13:", ll.search(13))
print("Search for 2:", ll.search(2)) #Should return -1