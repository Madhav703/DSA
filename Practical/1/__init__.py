# Program for using Dynamic Functions (malloc(), calloc(), realloc() and free()) functions.

n = 5
memory = [None] * n
print("After malloc simulation:", memory)

memory = [0] * n
print("After calloc simulation:", memory)

new_size = 8
try:
    if new_size > len(memory):
        memory.extend( * (new_size - len(memory)))  
    else:
        memory = memory[:new_size] 
    print("After realloc simulation:", memory)

    memory = None
    print("After free simulation:", memory)

except:
    pass
