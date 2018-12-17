"""" Without try-except

The try block tests the block of code for errors.
The except block handles the error.
The finally block executes a block of code, regardless of the result of the try- and except blocks.
"""

if __name__ == "__main__":
    x = int(input("Please enter a number: "))
    y = 1/x
    print("Just after 1/x")
