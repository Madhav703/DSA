# Program to insert, delete and traverse an element from an array

def insert_element(arr, element, position):
    if position < 0 or position > len(arr):
        raise IndexError("Position out of bounds")
    return arr[:position] + [element] + arr[position:]

def delete_element(arr, position):
    if position < 0 or position >= len(arr):
        raise IndexError("Position out of bounds")
    return arr[:position] + arr[position + 1:]

def traverse_array(arr):
    for i, element in enumerate(arr):
        print(f"Element at index {i}: {element}")

arr = [1, 2, 3, 4, 5]
print("Original array:", arr)
arr = insert_element(arr, 6, 2)
print("Array after insertion:", arr)
arr = delete_element(arr, 2)
print("Array after deletion:", arr)
print("Traversing the array:")
traverse_array(arr)