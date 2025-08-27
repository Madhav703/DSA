# Program to find the number of vowels, consonants, digits and white space in a string.

import asyncio

async def count_vowels(m):
    vowels  = "aieou"
    count = 0
    for _ in m:
        if _ in vowels:
            count = count + 1
    print("Numbers of vowels in {}: {}".format(m, count))
    
async def count_const(m):
    const = "bcdfghjklmnpqrstvwxyz"
    count = 0
    for _ in m:
        if _ in const:
            count += 1
    
    print("Consonants in {}: {}".format(m, count))
    
async def count_digits(m):
    digits = "1234567890"
    count = 0
    for _ in m:
        if _ in digits:
            count = count + 1
    
    print("Digits in {}: {}".format(m, count))
    
async def count_white_space(m):
    space = " "
    count = 0
    for _ in m:
        if _ in space:
            count = count + 1
        
    print("White space in {}: {}".format(m, count))
    
async def main():
    m = input("Enter a string: ").replace(" ","").lower()
    await count_vowels(m)
    await count_const(m)
    await count_digits(m)
    await count_white_space(m)
    
if __name__ == "__main__":
    asyncio.run(main())