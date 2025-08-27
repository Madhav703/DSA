# Program to calculate length of the string using user defined function.

import asyncio

async def count_string(string):
    count = 0
    for c in string:
        count = count + 1
    return count


async def main():
    m = input("Enter a string: ")
    print(f"The length of the string {m} is {await count_string(m)}")
    
if __name__ == "__main__":
    asyncio.run(main())