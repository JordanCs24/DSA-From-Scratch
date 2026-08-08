class dynamicArray:
    def __init__(self):
        self.size = 0
        self.capacity = 1
        self.array = [None]
    def append(self, data):
        if (self.size == self.capacity):
            new_capacity = self.capacity * 2
            new_array = [None] * new_capacity
            for i in range(self.size):
                new_array[i] = self.array[i]
            self.array = new_array
            self.capacity = new_capacity
        self.array[self.size] = data #add data
        self.size +=1
    def __getitem__(self, index):
        if (index >= self.size):
            raise IndexError("index out of range")
        if (index < 0):
            raise IndexError("index out of range")
        return self.array[index]
    def __setitem__(self,index,data):
        if (index < 0):
            raise IndexError("index out of range")
        if (index >= self.size):
            raise IndexError("index out of range")
        self.array[index] = data
    def __len__(self):
        return self.size
    def pop(self):
        if (self.size <= 0):
            raise IndexError("index out of range")
        extracted_data = self.array[self.size - 1]
        self.array[self.size - 1] = None
        self.size -= 1
        return extracted_data

#Smoke Tests 
arr = dynamicArray()
for x in [10, 20, 30, 40, 50]:
    arr.append(x)
print(arr.array, arr.size, arr.capacity)

arr = dynamicArray()
for x in [10, 20, 30]:
    arr.append(x)
print(arr[1])          # 20 — proves __getitem__ is wired
arr[1] = 99            # proves __setitem__ is wired
print(arr.pop())       # 30
print(len(arr) == 2)   # True — proves pop decremented