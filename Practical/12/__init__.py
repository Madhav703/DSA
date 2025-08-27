# Program to concatenate and compare two strings using user defined function.

def compare_strings(str1, str2):
    if str1 == str2:
        return "The strings are equal."
    else:
        return "The strings are not equal."

str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")
print(compare_strings(str1, str2))

print(f"Concatenated string: {str1+str2}")
print(f"Comparison result: {compare_strings(str1, str2)}")
    
    