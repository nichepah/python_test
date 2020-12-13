#!/bin/python

def maximum(a, b):
    """The furnction returns larger of the two numbers passed.

    :param a: First number
    :param b: Second number
    :return: Larger of the two is returned
    """
    if a >= b:
        return a
    else:
        return b


if __name__ == "__main__":
    """ This is the main function.

    """
    a = 2
    b = 4
    print(maximum(a, b))
