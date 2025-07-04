class Node:
    def __init__(self, data):
        self.data = data
        self.next = self
        self.prev = self

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            tail = self.head.prev
            tail.next = new_node
            new_node.prev = tail
            new_node.next = self.head
            self.head.prev = new_node

    def display(self):
        if not self.head:
            return
        temp = self.head
        while True:
            print(temp.data, end=" <-> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(Back to head)")

cdll = CircularDoublyLinkedList()
cdll.insert(10)
cdll.insert(20)
cdll.insert(30)
cdll.display()
