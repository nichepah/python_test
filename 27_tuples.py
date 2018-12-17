if __name__ == "__main__":
    """ Demo tuples.

    A tuple consists of a number of values separated by commas
    Tuples are immutable
    """
    my_tuple = 1, 2, 4, 5
    print(my_tuple)
    # tuples can be nested
    my_nested_tuple = 11, 12, my_tuple
    print(my_nested_tuple)
    # error
    # my_tuple[0] = 100
    # some quirks of tuples: for empty use ();
    # for single value initialization use a comma - think: Can we drop the comma?: check type(b) in both cases
    a = ()
    b = 11,
    # tuple packing
    a = 1, 2, 3, 'india'
    # reverse is sequence unpacking
    x, y , z, n = a
    print(x, y, z, n)

