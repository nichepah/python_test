if __name__ == "__main__":
    """ Explanation on id and type in the context of mutable and immutable

    Objects of int, float, bool, str, tuple are immutable
    Objects of list, set, dict are mutable.
    
    id() returns the identity of the obj as an integer
    type() returns the type
    
    Shows difference between int and list in the context of mutability
    """
    a = "ranchi"
    b = "ranchi"
    print(type(a))
    # use 'is' operator
    print(a is b)
    # or use your familiar 'if'
    if id(a) == id(b):
        print("ids are the same")
    else:
        print("diff ids")
    # consider id of x, and 100 which is an immutable object
    x = 100
    y = x
    print("x is 100, y is x", x is 100, y is x)
    print("id(x), id(100), id(y)", id(x), id(100), id(y))
    x = x - 1
    print("x = x - 1")
    print("x is 100", x is 100)
    print("id(x), id(100), id(y)", id(x), id(100), id(y))
    print("id(100) remains the same...object 100 is immutable")
    # consider lists
    print("Lists are mutable")
    list_1 = list([1, 2, 3])
    list_2 = list_1
    print("list_1", list_1)
    print("list_1 is list_2", list_1 is list_2)
    list_1.pop()
    print("list_1 changed", list_1)
    print("list_1 is list_2", list_1 is list_2)
    # note to anurag: control flow doesn't go back to #33 after #35; its just that the list_1 and list_2 point
    # to the same list

