
class Test:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        
    def __str__(self):
        return "Hello %s, you are %d years old!" %(self.name, self.age)
    
age = int(input("Enter your age: "))
name = input("Enter your name: ")
run = Test(name, age)
print(run)