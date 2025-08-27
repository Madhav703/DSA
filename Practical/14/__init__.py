# Program to reverse a sentence using recursion.

async def reverse(string):
    if len(string) <= 1:
        return string
    else:
        return string[1:] + string[0]
    

async def main():
    _ = input("Enter a string: ")
    print(f"Reversed string: {await reverse(_)}")
    
if __name__ ==  "__main__":
    import asyncio
    asyncio.run(main())