def prime(n):
    """ Prints prime numbers less than n.

    :param n:
    :return:
    """
    print("Prime numbers: ")
    for i in range(2, n):
        for j in range(2, i):
            if i % j == 0:
                break
        # this else belongs to the for loop, and runs when no break is executed, for like else in a try clause
        else:
            print(i, end=',')


if __name__ == "__main__":
    prime(int(input("Please enter a number: ")))

