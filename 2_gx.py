# !/bin/python

# range function uses list
def g(x):
    """
    Prints g(x) = x/(1-x)^2, for values i%2==1

    :param x: The range
    :return: Returns float
    """
    for i in range(10):
        x = 0.1 * i
        print(x / (1 - x * x))


if __name__ == "__main__":
    """
    The main
    
    """
    for i in range(10):
        if i % 2 == 1:
            print(i)
            print(g(0.1 * i))

