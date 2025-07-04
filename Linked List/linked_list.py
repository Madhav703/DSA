class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after(self, prev_data, data):
        temp = self.head
        while temp and temp.data != prev_data:
            temp = temp.next
        if not temp:
            print("Previous node not found")
            return
        new_node = Node(data)
        new_node.next = temp.next
        temp.next = new_node

    def delete(self, key):
        temp = self.head

        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return

        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if not temp:
            print("Node not found")
            return

        prev.next = temp.next
        temp = None

    def search(self, key):
        temp = self.head
        while temp:
            if temp.data == key:
                return True
            temp = temp.next
        return False

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


ll = LinkedList()
ll.append(10)
ll.append(20)
ll.prepend(5)
ll.insert_after(10, 15)
ll.display()  

ll.delete(15)
ll.display()  

print("Search 10:", ll.search(10))  
print("Search 99:", ll.search(99))  