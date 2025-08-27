# Program for using the concept of pointer to string.

import asyncio

async def pointer_to_string(m: str):
    print(f"Your string: {m}")
    
    for _ in range(len(m)):
        print(f"Pointer at index {_+1}: {m[_]}")
        
async def new():
    string = input("Enter a string: ")
    await pointer_to_string(string)

if __name__ == "__main__":
    asyncio.run(new())