if __name__ == "__main__":
    """Program to get a number from user, and print whether it is negative, positive, or zero.
     
     Use elif"""
    n = int(input(" Please enter a number: "))
    if n < 0:
        print("negative")
    elif n > 0:
        print("positive")
    else:
        print("zero")
