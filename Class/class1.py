class myClass:
    def __init__(self, name: str, age: int):
        self.age = age
        self.name = name
    
    def take_input(self):
        name = input('Please enter your name: ')
        age = int(input("Please enter your age: "))
        self.name = name
        self.age = age
    
    def show_output(self):
        print(f"Hello {self.name} you are {self.age} years old!")
    
run = myClass("\n", 0)
run.take_input()
run.show_output()