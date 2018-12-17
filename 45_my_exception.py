"""" On try-except-finally.

The try block tests the block of code for errors.
The except block handles the error.
The finally block executes a block of code, regardless of the result of the try- and except blocks.
"""

if __name__ == "__main__":
    try:
        x = int(input("Please enter a number: "))
        y = 1/x
        print("In try block")
    except ZeroDivisionError:
        print(" Zero div ")
    finally:
        print("Always printed finally")

    print("out of the exception blocks")
