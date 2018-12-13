if __name__ == "__main__":
    """Program to check if a number is prime or not.
    
    Break outs from the smallest enclosing for or while loop
    pay attention to the else clause which belongs to the for loop.
    """
    for i in range(1, 100):
        for j in range(2, i):
            if i % j == 0:
                break
        # this else belongs to the for loop, and runs when no break is executed, for like else in a try clause
        else:
            print(i, " is a prime")
