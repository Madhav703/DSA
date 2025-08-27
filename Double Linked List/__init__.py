
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        
    def insert(self, data):
        new_node = Node(data)
        
        if not self.head:
            self.head = new_node
            return
        
        temp = self.head
        
        while temp.next:
            temp = temp.next
            
        temp.next = new_node
        new_node.prev = temp
        
    def display(self):
        temp = self.head
        
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")
        
a = DoublyLinkedList()
a.insert(1)
a.insert(2)
a.insert(3)
a.insert(4)
a.insert(5)
a.display()

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#         self.prev = None

# class DoublyLinkedList:
#     def __init__(self):
#         self.head = None
    
#     def insert(self, data):
#         new_node = Node(data)
#         if not self.head:
#             self.head = new_node
#             return
        
#         temp = self.head
#         while temp.next:
#             temp = temp.next
#         temp.next = new_node
#         new_node.prev = temp
        
#     def display(self):
#         temp = self.head
#         while temp:
#             print(temp.data, end=" <-> ")
#             temp = temp.next
#         print("None")
        
        
# m = DoublyLinkedList()
# m.insert(1)
# m.insert(2)
# m.insert(3)
# m.insert(4)
# m.insert(5)
# m.display()
