from math import pi

if __name__ == "__main__":
    """ Demo List comprehension.

    Print value of pi in increasing order of precision from 1 to 10 decimal places
    Uses a for loop for definition
    """
    my_pi_list = [round(pi, i) for i in range(1, 10)]
    print(my_pi_list)