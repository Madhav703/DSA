# make an akinator game

class CharacterNode:
    def __init__(self, question=None, character=None):
        self.question = question
        self.character = character
        self.yes = None
        self.no = None

def get_user_name():
    name = input("What is your name? ")
    return name

def get_user_response():
    while True:
        response = input("Enter 'yes' or 'no': ").lower()
        if response in ['yes', 'no']:
            return response == 'yes'
        print("Please enter either 'yes' or 'no'.")

def create_decision_tree():
    root = CharacterNode("Is your character from a superhero movie/comic?")
    
    root.yes = CharacterNode("Does your character wear a red suit?")
    root.yes.yes = CharacterNode(character="Spider-Man")
    root.yes.no = CharacterNode("Can your character fly?")
    root.yes.no.yes = CharacterNode(character="Superman")
    root.yes.no.no = CharacterNode(character="Batman")
    
    root.no = CharacterNode("Is your character from a fantasy world?")
    root.no.yes = CharacterNode("Is your character a wizard?")
    root.no.yes.yes = CharacterNode(character="Harry Potter")
    root.no.yes.no = CharacterNode(character="Frodo Baggins")
    root.no.no = CharacterNode("Is your character an animated character?")
    root.no.no.yes = CharacterNode(character="Mickey Mouse")
    root.no.no.no = CharacterNode(character="James Bond")
    
    return root

def play_game(node):
    if node.character:
        print(f"I guess your character is {node.character}!")
        correct = get_user_response()
        if correct:
            print("Great! I guessed it correctly!")
        else:
            print("Oh no! I got it wrong. Maybe next time!")
        return
    
    print(node.question)
    if get_user_response():
        play_game(node.yes)
    else:
        play_game(node.no)

def start_game():
    print("Welcome to the Akinator game!")
    user_name = get_user_name()
    print(f"Hello, {user_name}! Let's start the game.")
    print("Think of a character, and I will try to guess it by asking you questions.")
    print("Ready? Let's begin!")
    
    decision_tree = create_decision_tree()
    play_game(decision_tree)
    
    while True:
        print("\nWould you like to play again?")
        if not get_user_response():
            print("Thanks for playing!")
            break
        print("\nOK, let's play again!")
        play_game(decision_tree)

start_game()
