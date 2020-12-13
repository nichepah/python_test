def square_sum(n):
    """This furnction calculates sum of squares of first n natural numbers.

    :param n: The number up to which has to be squared
    :return: Sum of all squares up to n
    """
    my_sum = 0
    for i in range(n+1):
        my_sum = my_sum + (i * i)
    return my_sum


if __name__ == "__main__":
    """ This is the main function.

    """
    print(square_sum(10))
