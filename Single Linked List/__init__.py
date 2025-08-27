
# This is a simple program to create a list where each item points to the next item

# This is like a container for storing one piece of data
class Box:
    def __init__(self, item):
        self.item = item    # The item we want to store
        self.next = None    # Link to the next box

# This is our list that connects all boxes together
class MyList:
    def __init__(self):
        self.first_box = None    # We start with no boxes
    
    # Add a new item to our list
    def add_item(self, item):
        # Pack the item in a new box
        new_box = Box(item)
        
        # If this is our first item
        if self.first_box is None:
            self.first_box = new_box
            return
        
        # Find the last box
        current_box = self.first_box
        while current_box.next is not None:
            current_box = current_box.next
            
        # Connect the new box at the end
        current_box.next = new_box
    
    # Show all items in our list
    def show_all(self):
        current_box = self.first_box
        
        while current_box is not None:
            print(current_box.item, end=" → ")
            current_box = current_box.next
        print("END")

# Let's try it out!
my_list = MyList()

# Add some numbers to our list
print("Adding numbers to the list...")
my_list.add_item(1)
my_list.add_item(2)
my_list.add_item(3)

# Show what's in our list
print("\nHere's what's in our list:")
my_list.show_all()
            


