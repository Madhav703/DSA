# Program to delete all repeated words in string.

import asyncio

def remove_repeated_words(text: str) -> str:
    words = text.split()
    seen = set()
    result = []
    for word in words:
        if word not in seen:
            seen.add(word)
            result.append(word)
    return " ".join(result)

s = input("Enter a string: ")
print("Without repeats:", remove_repeated_words(s))
