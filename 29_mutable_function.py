def function_1(list, my_string):
    """ Appends my_string to list

    :param list:
    :param my_string:
    """
    list.append(my_string)
    print("function_1, id(l)", id(l))


def function_2(n, a):
    """ Increments n by a

    """
    n + a
    print("function_2: id(n + a)", id(n + a))


if __name__ == "__main__":
    """ Shows diff in passing a mutable/immutable to a function

    Implement 2 separate functions: function_1 to append a value to a list of int, function_2 to increment an int.
    In both functions pass the parent object.
    
    Mutables passed by ref, immutable passed by val\
    Pay attention to prins from within the functions; in case of mutable id remains the same as in the callee.
    """
    l = list(['a', 'b', 'c'])
    print(l)
    print("id(l)", id(l))
    function_1(l, 'd')
    print(l)
    print("id(l)", id(l))
    n = 100
    print(n)
    print("id(n)", id(n))
    function_2(n, 1)
    print(n)
    print("id(n)", id(n))

